from typing import List, Dict, Any, Optional
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue, SearchRequest
from chunking.splitter import Chunk
import sys
sys.path.append('.')
from config import settings


class QdrantManager:
    """Manage vector storage using Qdrant"""
    
    def __init__(self, location: str = ":memory:"):
        # Initialize Qdrant client (in-memory mode)
        self.client = QdrantClient(location=location)
        self.collection_name = settings.qdrant_collection_name
    
    def create_collection(self, vector_size: int):
        """Create a new collection"""
        # Check if collection exists
        collections = self.client.get_collections().collections
        collection_names = [c.name for c in collections]
        
        if self.collection_name in collection_names:
            return
        
        # Create collection
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )
    
    def store_chunks(self, chunks: List[Chunk], embeddings: List[List[float]]):
        """Store chunks with their embeddings in Qdrant"""
        points = []
        
        for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            point = PointStruct(
                id=chunk.chunk_id,
                vector=embedding,
                payload={
                    "content": chunk.content,
                    **chunk.metadata
                }
            )
            points.append(point)
        
        # Insert points in batches
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
    
    def search(
        self,
        query_vector: List[float],
        limit: int = 5,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Search for similar vectors"""
        # Build filter if provided
        query_filter = None
        if filters:
            conditions = []
            for key, value in filters.items():
                conditions.append(
                    FieldCondition(
                        key=key,
                        match=MatchValue(value=value)
                    )
                )
            query_filter = Filter(must=conditions)
        
        # Search
        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            query_filter=query_filter,
            limit=limit,
            with_payload=True,
            with_vectors=False
        ).points
        
        # Format results
        formatted_results = []
        for result in results:
            formatted_results.append({
                "id": result.id,
                "score": result.score,
                "content": result.payload.get("content"),
                "metadata": {k: v for k, v in result.payload.items() if k != "content"}
            })
        
        return formatted_results
    
    def get_collection_info(self) -> Dict[str, Any]:
        """Get information about the collection"""
        try:
            info = self.client.get_collection(self.collection_name)
            return {
                "name": self.collection_name,
                "points_count": info.points_count,
                "vector_size": info.config.params.vectors.size
            }
        except Exception as e:
            return {}
