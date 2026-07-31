from pathlib import Path
from typing import Dict, Any
from ingestion.parser import Document
import sys
sys.path.append('.')
from rag_logging.logger import log_metadata, setup_logger


class MetadataManager:
    """Enrich documents with structured metadata"""
    
    def __init__(self):
        self.logger = setup_logger("metadata_manager")
        
        # Department mapping based on folder structure
        self.department_mapping = {
            "HR": "HR",
            "IT": "IT",
            "Engineering": "Engineering",
            "Company": "Company",
        }
        
        # Document type mapping based on file extension
        self.document_type_mapping = {
            ".pdf": "PDF",
            ".docx": "Document",
            ".md": "Markdown",
            ".csv": "Spreadsheet",
            ".json": "Data",
        }
    
    def extract_department(self, file_path: Path) -> str:
        """Extract department from file path"""
        for folder_name, department in self.department_mapping.items():
            if folder_name in file_path.parts:
                return department
        return "General"
    
    def extract_document_type(self, file_path: Path) -> str:
        """Extract document type from file extension"""
        suffix = file_path.suffix.lower()
        return self.document_type_mapping.get(suffix, "Unknown")
    
    def extract_document_name(self, file_path: Path) -> str:
        """Extract document name from file path"""
        return file_path.stem
    
    def detect_language(self, content: str) -> str:
        """Simple language detection (default to English)"""
        # In production, use a proper language detection library
        return "English"
    
    def enrich_document(self, document: Document) -> Document:
        """Enrich a document with metadata"""
        file_path = Path(document.source)
        
        # Extract metadata
        metadata = {
            "department": self.extract_department(file_path),
            "document_name": self.extract_document_name(file_path),
            "document_type": self.extract_document_type(file_path),
            "language": self.detect_language(document.content),
            "total_pages": document.page_number,  # Will be updated during chunking
        }
        
        # Merge with existing metadata
        document.metadata.update(metadata)
        
        # Log metadata
        log_metadata(
            self.logger,
            document.metadata.get("document_name", "Unknown"),
            document.metadata
        )
        
        return document
    
    def enrich_documents(self, documents: list) -> list:
        """Enrich multiple documents with metadata"""
        enriched = []
        for doc in documents:
            enriched_doc = self.enrich_document(doc)
            enriched.append(enriched_doc)
        return enriched
