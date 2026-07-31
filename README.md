# Enterprise Knowledge Assistant (RAG)

A production-style Retrieval-Augmented Generation (RAG) application that answers questions from an organization's internal knowledge base.

## Features

- **Multi-format Document Support**: PDF, DOCX, Markdown, CSV, JSON
- **Metadata Enrichment**: Automatic extraction of department, document type, and other metadata
- **Intelligent Chunking**: Recursive character text splitting with overlap
- **Semantic Search**: Vector embeddings using BAAI/bge-small-en-v1.5
- **Query Understanding**: LLM-powered metadata filter extraction
- **Context Augmentation**: RAG prompt building with retrieved context
- **Grounded Answers**: Gemini LLM with citation instructions
- **Evaluation**: RAGAS metrics for measuring pipeline quality
- **Observability**: Langfuse integration for tracing and monitoring
- **Structured Logging**: JSON logging for each pipeline stage

## Tech Stack

- **Backend**: Python, FastAPI
- **LLM**: Google Gemini (gemini-1.5-flash)
- **Embeddings**: BAAI/bge-small-en-v1.5
- **Vector Database**: Qdrant (in-memory)
- **Framework**: LangChain
- **Evaluation**: RAGAS
- **Observability**: Langfuse
- **UI**: Streamlit

## Installation

1. **Clone the repository**
```bash
cd rag
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
# Copy the example .env file
# Edit .env and add your API keys
```

Required environment variables:
- `GEMINI_API_KEY`: Get from https://makersuite.google.com/app/apikey (free)
- `LANGFUSE_PUBLIC_KEY`: Optional, get from https://langfuse.com
- `LANGFUSE_SECRET_KEY`: Optional, get from https://langfuse.com

## Project Structure

```
enterprise-rag/
├── app.py                          # Main orchestration script
├── config.py                       # Configuration management
├── .env                            # Environment variables
├── requirements.txt                # Python dependencies
├── data/                           # Knowledge base documents
│   ├── HR/                         # HR documents
│   ├── IT/                         # IT documents
│   ├── Engineering/                # Engineering documents
│   ├── Company/                    # Company documents
│   └── Images/                     # Images
├── ingestion/                      # Document loading
│   ├── loaders.py                  # File loaders
│   └── parser.py                   # Document parser
├── metadata/                       # Metadata enrichment
│   └── metadata_manager.py         # Metadata extraction
├── chunking/                       # Text chunking
│   └── splitter.py                 # Document splitter
├── embeddings/                     # Embedding generation
│   └── embedder.py                 # Embedding model
├── vectordb/                       # Vector storage
│   └── qdrant_client.py            # Qdrant client
├── retrieval/                      # Retrieval
│   ├── query_understanding.py      # Query analysis
│   └── retriever.py                # Vector search
├── prompting/                      # Prompt building
│   └── prompt_builder.py           # RAG prompt builder
├── generation/                     # Answer generation
│   └── llm.py                      # LLM interface
├── evaluation/                     # Evaluation
│   └── ragas_eval.py               # RAGAS metrics
├── observability/                  # Observability
│   └── langfuse.py                 # Langfuse tracing
├── logging/                        # Logging
│   └── logger.py                   # Structured logger
├── ui/                             # User interface
│   └── streamlit_app.py            # Streamlit UI
└── utils/                          # Utilities
```

## Usage

### Command Line Interface

**Ingest documents into vector database:**
```bash
python app.py --ingest
```

**Ask a question:**
```bash
python app.py --query "How many annual leave days do employees get?"
```

**Custom data directory:**
```bash
python app.py --ingest --data-dir /path/to/documents
```

**Adjust retrieval count:**
```bash
python app.py --query "What is the VPN setup process?" --top-k 3
```

### Streamlit UI

**Launch the web interface:**
```bash
streamlit run ui/streamlit_app.py
```

The UI provides:
- Chat interface asking questions
- Display of retrieved context chunks
- Response time metrics
- Adjustable Top-K settings
- Example questions

## Pipeline Stages

### Phase 1: Document Ingestion
Loads documents from multiple formats (PDF, DOCX, MD, CSV, JSON) and normalizes them into unified Document objects.

**Logging:**
```
Loading employee_handbook.md
Pages: 1
Characters: 4,521
Status: Success
```

### Phase 2: Metadata Enrichment
Attaches structured metadata to documents including department, document type, language, and source.

**Logging:**
```
Document: employee_handbook
Metadata:
  Department: HR
  Type: Markdown
  Language: English
```

### Phase 3: Chunking
Splits documents into meaningful chunks using Recursive Character Text Splitter with configurable size and overlap.

**Logging:**
```
Chunk Size: 500
Overlap: 100
Generated Chunks: 15
```

### Phase 4: Embedding Generation
Converts text chunks into vector embeddings using BAAI/bge-small-en-v1.5 (384 dimensions).

**Logging:**
```
Embedding Model: BAAI/bge-small-en-v1.5
Dimensions: 384
Chunks Embedded: 74
Time: 2.1 sec
```

### Phase 5: Vector Storage
Stores vectors and metadata in Qdrant vector database.

**Logging:**
```
Collection: enterprise_docs
Vectors Stored: 74
Payload Stored: Yes
```

### Phase 6: Query Understanding
Uses LLM to extract metadata filters from user queries when appropriate.

**Logging:**
```
User Query: How many leaves do employees get?
Extracted Filters:
  Department: HR
  Type: Policy
```

### Phase 7: Retrieval
Performs vector search with optional metadata filters to retrieve relevant chunks.

**Logging:**
```
Applied Filter: Department = HR
Top K: 5
Retrieved:
  Chunk 21 - Score: 0.94
  Chunk 8 - Score: 0.89
```

### Phase 8: Context Augmentation
Builds the RAG prompt combining question, retrieved context, and instructions.

**Logging:**
```
Prompt:
  Question: ...
  Context: Chunk 21, Chunk 8, Chunk 4
  Instructions: ...
```

### Phase 9: Answer Generation
Generates grounded answers using Gemini LLM with instructions to cite sources and avoid hallucination.

**Logging:**
```
Model: gemini-1.5-flash
Prompt Tokens: 1,240
Completion Tokens: 181
Latency: 2.3 sec
```

### Phase 10: Evaluation
Measures RAG pipeline quality using RAGAS metrics (Faithfulness, Answer Relevancy, Context Precision, Context Recall).

**Logging:**
```
Faithfulness: 0.96
Answer Relevancy: 0.91
Context Precision: 0.88
```

### Phase 11: Observability
Traces complete request lifecycle using Langfuse for production monitoring and debugging.

**Features:**
- Complete trace of each request
- Retrieved chunks with scores
- Prompt and response
- Latency and token usage
- Cost tracking
- Evaluation metrics

## Sample Knowledge Base

The project includes a realistic enterprise knowledge base:

**HR Department:**
- Employee Handbook
- Leave Policy

**IT Department:**
- VPN Setup Guide
- Laptop Troubleshooting
- Printer Setup Guide

**Engineering Department:**
- API Reference (JSON)
- Deployment Guide

**Company:**
- Holidays (CSV)
- FAQ

## Configuration

Edit `config.py` or environment variables to customize:

- **Chunking**: `CHUNK_SIZE`, `CHUNK_OVERLAP`
- **Retrieval**: `TOP_K`
- **LLM**: `LLM_MODEL`, `LLM_TEMPERATURE`
- **Embeddings**: `EMBEDDING_MODEL`, `EMBEDDING_DEVICE`
- **Qdrant**: `QDRANT_HOST`, `QDRANT_PORT`

## Development

### Adding New Document Types

1. Add loader in `ingestion/loaders.py`
2. Update file extension mapping in `DocumentLoader.load_document()`

### Adding New Metadata Fields

1. Update `metadata/metadata_manager.py`
2. Add extraction logic in `enrich_document()`

### Custom Evaluation Metrics

1. Add metrics to `evaluation/ragas_eval.py`
2. Update evaluation pipeline in `app.py`

## Troubleshooting

**Import errors:**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`

**Embedding model download issues:**
- Model downloads automatically on first run
- Ensure internet connection is available
- Model size: ~100MB

**Qdrant connection issues:**
- Default uses in-memory mode (no server needed)
- For Docker: `docker run -p 6333:6333 qdrant/qdrant`

**Gemini API errors:**
- Verify `GEMINI_API_KEY` is set in `.env`
- Get free key from https://makersuite.google.com/app/apikey

## License

This project is for educational purposes.

## Acknowledgments

- LangChain for the framework
- Qdrant for vector database
- BAAI for embedding model
- Google for Gemini LLM
- RAGAS for evaluation metrics
