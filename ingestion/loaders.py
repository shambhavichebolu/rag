from pathlib import Path
from typing import List, Dict, Any
import pypdf
from docx import Document
import json
import csv


class DocumentLoader:
    """Base class for document loaders"""
    
    @staticmethod
    def load_pdf(file_path: Path) -> List[Dict[str, Any]]:
        """Load PDF document"""
        pages = []
        with open(file_path, 'rb') as file:
            pdf_reader = pypdf.PdfReader(file)
            for page_num, page in enumerate(pdf_reader.pages):
                text = page.extract_text()
                if text.strip():
                    pages.append({
                        "page_number": page_num + 1,
                        "content": text,
                        "source": str(file_path)
                    })
        return pages
    
    @staticmethod
    def load_docx(file_path: Path) -> List[Dict[str, Any]]:
        """Load DOCX document"""
        pages = []
        doc = Document(file_path)
        full_text = []
        
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                full_text.append(paragraph.text)
        
        # Treat entire document as one page for simplicity
        if full_text:
            pages.append({
                "page_number": 1,
                "content": "\n".join(full_text),
                "source": str(file_path)
            })
        
        return pages
    
    @staticmethod
    def load_markdown(file_path: Path) -> List[Dict[str, Any]]:
        """Load Markdown document"""
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        return [{
            "page_number": 1,
            "content": content,
            "source": str(file_path)
        }]
    
    @staticmethod
    def load_csv(file_path: Path) -> List[Dict[str, Any]]:
        """Load CSV document"""
        content = []
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                content.append(str(row))
        
        full_content = "\n".join(content)
        
        return [{
            "page_number": 1,
            "content": full_content,
            "source": str(file_path)
        }]
    
    @staticmethod
    def load_json(file_path: Path) -> List[Dict[str, Any]]:
        """Load JSON document"""
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        content = json.dumps(data, indent=2)
        
        return [{
            "page_number": 1,
            "content": content,
            "source": str(file_path)
        }]
    
    @classmethod
    def load_document(cls, file_path: Path) -> List[Dict[str, Any]]:
        """Load document based on file extension"""
        suffix = file_path.suffix.lower()
        
        loaders = {
            '.pdf': cls.load_pdf,
            '.docx': cls.load_docx,
            '.md': cls.load_markdown,
            '.csv': cls.load_csv,
            '.json': cls.load_json,
        }
        
        loader = loaders.get(suffix)
        if loader is None:
            raise ValueError(f"Unsupported file type: {suffix}")
        
        return loader(file_path)
