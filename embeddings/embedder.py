from typing import List
from sentence_transformers import SentenceTransformer
import time
from chunking.splitter import Chunk
import sys
sys.path.append('.')
from config import settings
from rag_logging.logger import log_embeddings, setup_logger


class Embedder:
    """Generate embeddings for text chunks using all-MiniLM-L6-v2"""
    
    def __init__(self, model_name: str = None, device: str = None):
        self.model_name = model_name or settings.embedding_model
        self.device = device or settings.embedding_device
        self.logger = setup_logger("embedder")
        
        # Load the model (let SentenceTransformer handle device automatically)
        self.logger.info(f"Loading embedding model: {self.model_name}")
        self.model = SentenceTransformer(self.model_name)
        self.dimensions = self.model.get_sentence_embedding_dimension()
        
        self.logger.info(f"Model loaded. Dimensions: {self.dimensions}")
    
    def embed_chunks(self, chunks: List[Chunk]) -> List[List[float]]:
        """Generate embeddings for a list of chunks"""
        start_time = time.time()
        
        # Extract text from chunks
        texts = [chunk.content for chunk in chunks]
        
        # Generate embeddings
        embeddings = self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True
        )
        
        time_taken = time.time() - start_time
        
        # Log embedding details
        log_embeddings(
            self.logger,
            self.model_name,
            self.dimensions,
            len(chunks),
            time_taken
        )
        
        return embeddings.tolist()
    
    def embed_query(self, query: str) -> List[float]:
        """Generate embedding for a single query"""
        embedding = self.model.encode(query, convert_to_numpy=True)
        return embedding.tolist()
