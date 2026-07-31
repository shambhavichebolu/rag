from typing import List, Dict, Any, Optional
from embeddings.embedder import Embedder
from vectordb.qdrant_client import QdrantManager
from retrieval.query_understanding import QueryUnderstanding
import sys
sys.path.append('.')
from config import settings


class Retriever:
    """Retrieve relevant chunks using vector search with optional metadata filters"""

    def __init__(self, qdrant=None, embedder=None):
        self.embedder = embedder or Embedder()
        self.qdrant = qdrant or QdrantManager()
        self.query_understanding = QueryUnderstanding()
        self.top_k = settings.top_k
    
    def retrieve(self, query: str, top_k: int = None) -> List[Dict[str, Any]]:
        """Retrieve relevant chunks for a query"""
        top_k = top_k or self.top_k
        
        # Step 1: Understand the query and extract filters
        filters = {}
        if self.query_understanding.should_use_filters(query):
            filters = self.query_understanding.extract_filters(query)
        
        # Step 2: Embed the query
        query_vector = self.embedder.embed_query(query)
        
        # Step 3: Search in vector database
        results = self.qdrant.search(
            query_vector=query_vector,
            limit=top_k,
            filters=filters if filters else None
        )
        
        return results
    
    def retrieve_with_filters(
        self,
        query: str,
        filters: Dict[str, Any],
        top_k: int = None
    ) -> List[Dict[str, Any]]:
        """Retrieve with explicit filters"""
        top_k = top_k or self.top_k
        
        # Embed the query
        query_vector = self.embedder.embed_query(query)
        
        # Search with filters
        results = self.qdrant.search(
            query_vector=query_vector,
            limit=top_k,
            filters=filters
        )
        
        return results
