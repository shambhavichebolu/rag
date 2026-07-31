from typing import Dict, Any, Optional
import sys
sys.path.append('.')
from config import settings
from rag_logging.logger import log_query_understanding, setup_logger


class QueryUnderstanding:
    """Understand user queries and extract metadata filters using LLM"""
    
    def __init__(self):
        self.logger = setup_logger("query_understanding")
        self.model = None
        
        # Try to initialize with available LLM
        try:
            if settings.groq_api_key:
                from groq import Groq
                self.client = Groq(api_key=settings.groq_api_key)
                self.model = settings.llm_model
                self.logger.info("Query understanding using Groq")
            elif settings.gemini_api_key:
                import google.generativeai as genai
                genai.configure(api_key=settings.gemini_api_key)
                self.client = genai.GenerativeModel(settings.llm_model)
                self.model = settings.llm_model
                self.logger.info("Query understanding using Gemini")
            else:
                self.logger.warning("No LLM API key set. Query understanding disabled.")
        except Exception as e:
            self.logger.warning(f"Failed to initialize LLM for query understanding: {e}")
    
    def extract_filters(self, query: str) -> Dict[str, Any]:
        """Extract metadata filters from the query using LLM"""
        
        if not self.model:
            return {}
        
        # Define the prompt for filter extraction
        prompt = f"""
You are a metadata filter extractor for an enterprise knowledge base. 
Analyze the user's query and extract relevant metadata filters.

Available metadata fields:
- department: HR, IT, Engineering, Company
- document_type: PDF, Document, Markdown, Spreadsheet, Data

User Query: "{query}"

Extract filters ONLY if the query explicitly mentions a specific department or document type.
If the query is general or broad, return empty filters.

Return your answer as a JSON object with this format:
{{
    "department": "HR" or null,
    "document_type": "PDF" or null
}}

If a field is not mentioned, set it to null.
"""
        
        try:
            # Use Groq or Gemini based on what's available
            if settings.groq_api_key:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3
                )
                response_text = response.choices[0].message.content
            else:
                response = self.client.generate_content(prompt)
                response_text = response.text.strip()
            
            # Parse the response (simple JSON parsing)
            import json
            # Remove markdown code blocks if present
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            filters = json.loads(response_text)
            
            # Remove null values
            filters = {k: v for k, v in filters.items() if v is not None}
            
            # Log the extraction
            log_query_understanding(self.logger, query, filters)
            
            return filters
            
        except Exception as e:
            self.logger.error(f"Error extracting filters: {e}")
            return {}
    
    def should_use_filters(self, query: str) -> bool:
        """Determine if filters should be applied based on query"""
        # Simple heuristic: if query mentions specific department keywords
        department_keywords = ["HR", "IT", "Engineering", "Company", "human resources", "technology"]
        query_lower = query.lower()
        
        for keyword in department_keywords:
            if keyword.lower() in query_lower:
                return True
        
        return False
