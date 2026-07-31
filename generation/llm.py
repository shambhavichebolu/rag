import time
from groq import Groq
from typing import Dict, Any
import sys
sys.path.append('.')
from config import settings
from rag_logging.logger import log_generation, setup_logger


class LLMGenerator:
    """Generate answers using Groq LLM"""
    
    def __init__(self):
        self.logger = setup_logger("llm_generator")
        
        # Initialize Groq
        if settings.groq_api_key:
            self.client = Groq(api_key=settings.groq_api_key)
            self.model = settings.llm_model or "llama-3.3-70b-versatile"
            self.logger.info(f"Initialized Groq model: {self.model}")
        else:
            self.logger.warning("GROQ_API_KEY not set. LLM generation will not work.")
            self.client = None
            self.model = None
    
    def generate(self, prompt: str) -> Dict[str, Any]:
        """Generate an answer from the prompt"""
        
        if not self.model:
            return {
                "answer": "Error: GROQ_API_KEY not configured",
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "latency": 0
            }
        
        start_time = time.time()
        
        try:
            # Generate response
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=settings.llm_temperature
            )
            
            # Calculate latency
            latency = time.time() - start_time
            
            # Extract token usage
            prompt_tokens = response.usage.prompt_tokens
            completion_tokens = response.usage.completion_tokens
            
            # Log generation details
            log_generation(
                self.logger,
                self.model,
                prompt_tokens,
                completion_tokens,
                latency
            )
            
            return {
                "answer": response.choices[0].message.content,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "latency": latency,
                "model": self.model
            }
            
        except Exception as e:
            self.logger.error(f"Error generating answer: {e}")
            return {
                "answer": f"Error generating answer: {str(e)}",
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "latency": time.time() - start_time
            }
    
    def generate_with_system_prompt(self, system_prompt: str, user_prompt: str) -> Dict[str, Any]:
        """Generate with system prompt"""
        
        if not self.model:
            return {
                "answer": "Error: GROQ_API_KEY not configured",
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "latency": 0
            }
        
        start_time = time.time()
        
        try:
            # Generate response with system prompt
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=settings.llm_temperature
            )
            
            # Calculate latency
            latency = time.time() - start_time
            
            # Extract token usage
            prompt_tokens = response.usage.prompt_tokens
            completion_tokens = response.usage.completion_tokens
            
            # Log generation details
            log_generation(
                self.logger,
                self.model,
                prompt_tokens,
                completion_tokens,
                latency
            )
            
            return {
                "answer": response.choices[0].message.content,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "latency": latency,
                "model": self.model
            }
            
        except Exception as e:
            self.logger.error(f"Error generating answer: {e}")
            return {
                "answer": f"Error generating answer: {str(e)}",
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "latency": time.time() - start_time
            }
