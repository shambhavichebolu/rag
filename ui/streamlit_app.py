import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from retrieval.retriever import Retriever
from prompting.prompt_builder import PromptBuilder
from generation.llm import LLMGenerator
from observability.langfuse import LangfuseTracer
from vectordb.qdrant_client import QdrantManager
from embeddings.embedder import Embedder
import time
from app import RAGPipeline


def initialize_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'qdrant' not in st.session_state:
        st.session_state.qdrant = QdrantManager()
    if 'embedder' not in st.session_state:
        st.session_state.embedder = Embedder()
    if 'retriever' not in st.session_state:
        st.session_state.retriever = None
    if 'prompt_builder' not in st.session_state:
        st.session_state.prompt_builder = PromptBuilder()
    if 'llm' not in st.session_state:
        st.session_state.llm = LLMGenerator()
    if 'tracer' not in st.session_state:
        st.session_state.tracer = LangfuseTracer()
    if 'ingested' not in st.session_state:
        st.session_state.ingested = False


def ingest_documents():
    """Ingest documents into the vector database"""
    with st.spinner("Ingesting documents..."):
        try:
            from ingestion.parser import DocumentParser
            from metadata.metadata_manager import MetadataManager
            from chunking.splitter import DocumentSplitter
            from pathlib import Path

            # Use shared qdrant and embedder instances
            parser = DocumentParser()
            metadata_manager = MetadataManager()
            splitter = DocumentSplitter()

            # Parse documents
            documents = parser.parse_directory(Path("data"))
            enriched_documents = metadata_manager.enrich_documents(documents)
            chunks = splitter.split_documents(enriched_documents)

            # Generate embeddings
            embeddings = st.session_state.embedder.embed_chunks(chunks)

            # Create collection and store chunks
            st.session_state.qdrant.create_collection(st.session_state.embedder.dimensions)
            st.session_state.qdrant.store_chunks(chunks, embeddings)

            st.session_state.ingested = True
            st.session_state.retriever = Retriever(qdrant=st.session_state.qdrant, embedder=st.session_state.embedder)
            return True
        except Exception as e:
            st.error(f"Error ingesting documents: {str(e)}")
            return False


def load_pipeline():
    """Load the RAG pipeline components"""
    with st.spinner("Loading RAG pipeline..."):
        try:
            st.session_state.retriever = Retriever()
            return True
        except Exception as e:
            st.error(f"Error loading pipeline: {str(e)}")
            return False


def main():
    """Main Streamlit application"""
    st.set_page_config(
        page_title="Enterprise Knowledge Assistant",
        page_icon="🏢",
        layout="wide"
    )
    
    initialize_session_state()
    
    # Header
    st.title("🏢 Enterprise Knowledge Assistant")
    st.markdown("Ask questions about company policies, IT procedures, engineering documentation, and more.")
    
    # Ingest or load pipeline
    if not st.session_state.ingested:
        if st.button("Ingest Documents", type="primary"):
            if ingest_documents():
                st.success(f"Documents ingested successfully!")
                st.rerun()
    elif st.session_state.retriever is None:
        if st.button("Load Knowledge Base", type="primary"):
            if load_pipeline():
                st.success("Knowledge base loaded successfully!")
                st.rerun()
    else:
        st.success("✅ Knowledge base loaded")
    
    # Chat interface
    if st.session_state.retriever:
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
                # Show retrieved chunks for assistant messages
                if message["role"] == "assistant" and "chunks" in message:
                    with st.expander("📄 Retrieved Context"):
                        for idx, chunk in enumerate(message["chunks"]):
                            st.markdown(f"**Chunk {idx + 1}** (Score: {chunk['score']:.2f})")
                            st.markdown(f"*Source: {chunk['metadata'].get('document_name', 'Unknown')}*")
                            st.caption(chunk['content'][:300] + "..." if len(chunk['content']) > 300 else chunk['content'])
                    st.caption(f"⏱️ Response time: {message['latency']:.2f}s")
        
        # Chat input
        if prompt := st.chat_input("Ask a question about the company..."):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate response
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                message_placeholder.markdown("Thinking...")
                
                start_time = time.time()
                
                try:
                    # Create trace
                    trace = st.session_state.tracer.create_trace(prompt)
                    
                    # Retrieve relevant chunks
                    retrieved_chunks = st.session_state.retriever.retrieve(prompt, top_k=5)
                    
                    # Log retrieval span
                    st.session_state.tracer.log_retrieval(trace, prompt, retrieved_chunks, top_k=5)
                    
                    # Build prompt
                    rag_prompt = st.session_state.prompt_builder.build_rag_prompt(prompt, retrieved_chunks)
                    
                    # Generate answer
                    result = st.session_state.llm.generate(rag_prompt)
                    
                    latency = time.time() - start_time
                    
                    # Log generation span
                    st.session_state.tracer.log_generation(
                        trace,
                        rag_prompt,
                        result['answer'],
                        result['model'],
                        result['prompt_tokens'],
                        result['completion_tokens'],
                        latency
                    )
                    
                    # Display answer
                    message_placeholder.markdown(result['answer'])
                    
                    # Add assistant message
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": result['answer'],
                        "chunks": retrieved_chunks,
                        "latency": latency
                    })
                    
                    # End trace
                    st.session_state.tracer.end_trace(trace, result['answer'], {
                        "latency": latency,
                        "prompt_tokens": result['prompt_tokens'],
                        "completion_tokens": result['completion_tokens']
                    })
                    
                except Exception as e:
                    message_placeholder.markdown(f"Error: {str(e)}")
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": f"Error: {str(e)}",
                        "chunks": [],
                        "latency": time.time() - start_time
                    })
    
    # Sidebar
    with st.sidebar:
        st.header("About")
        st.markdown("""
        This assistant uses RAG (Retrieval-Augmented Generation) to answer questions from the company's knowledge base.
        
        **Features:**
        - Document retrieval from multiple departments
        - Metadata-aware filtering
        - Grounded answers with citations
        - Real-time observability
        """)
        
        st.header("Knowledge Base")
        if st.session_state.retriever:
            try:
                collection_info = st.session_state.retriever.qdrant.get_collection_info()
                st.metric("Documents", collection_info.get("points_count", 0))
                st.metric("Vector Size", collection_info.get("vector_size", 0))
            except:
                st.warning("Could not retrieve collection info")
        else:
            st.warning("Knowledge base not loaded")
        
        st.header("Settings")
        top_k = st.slider("Top K Results", min_value=1, max_value=10, value=5)
        if st.session_state.retriever:
            st.session_state.retriever.top_k = top_k
        
        st.header("Example Questions")
        example_questions = [
            "How many annual leave days do employees get?",
            "What is the VPN setup process?",
            "How do I request time off?",
            "What are the company's core values?",
            "How do I deploy to production?",
            "What is the printer IP address?",
        ]
        
        for question in example_questions:
            if st.button(question, key=question, use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": question})
                st.rerun()


if __name__ == "__main__":
    main()
