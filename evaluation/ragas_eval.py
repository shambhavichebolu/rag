from typing import List, Dict, Any
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_utilization, context_precision, context_recall
import sys
import os
sys.path.append('.')
from rag_logging.logger import log_evaluation, setup_logger
from config import settings


class RAGASEvaluator:
    """Evaluate RAG pipeline using RAGAS metrics"""
    
    def __init__(self):
        self.logger = setup_logger("ragas_evaluator")
        
        # Set OpenAI API key for RAGAS (required by the library)
        if settings.openai_api_key:
            os.environ["OPENAI_API_KEY"] = settings.openai_api_key
            self.logger.info("OpenAI API key set for RAGAS evaluation")
        else:
            self.logger.warning("OPENAI_API_KEY not set. RAGAS evaluation requires it.")
    
    def evaluate(
        self,
        questions: List[str],
        answers: List[str],
        contexts: List[List[str]],
        ground_truths: List[str] = None
    ) -> Dict[str, float]:
        """
        Evaluate RAG pipeline using RAGAS metrics
        
        Args:
            questions: List of user questions
            answers: List of generated answers
            contexts: List of retrieved contexts for each question
            ground_truths: List of ground truth answers (optional for some metrics)
        """
        
        # Prepare dataset
        data = {
            "question": questions,
            "answer": answers,
            "contexts": contexts,
        }
        
        if ground_truths:
            data["ground_truth"] = ground_truths
        
        dataset = Dataset.from_dict(data)
        
        # Define metrics
        metrics = [
            faithfulness,
            answer_relevancy,
            context_utilization,
        ]
        
        # Add context precision and recall if ground truths are available
        if ground_truths:
            metrics.extend([context_precision, context_recall])
        
        try:
            # Run evaluation
            result = evaluate(
                dataset=dataset,
                metrics=metrics
            )
            
            # Convert to dictionary
            scores = result.to_pandas().to_dict('records')[0]
            
            # Format scores
            formatted_scores = {}
            for key, value in scores.items():
                if hasattr(value, 'item'):  # Handle numpy types
                    formatted_scores[key] = float(value.item())
                elif isinstance(value, (int, float)):
                    formatted_scores[key] = float(value)
            
            # Log evaluation results
            log_evaluation(self.logger, formatted_scores)
            
            return formatted_scores
            
        except Exception as e:
            self.logger.error(f"Error during evaluation: {e}")
            return {}
    
    def evaluate_single(
        self,
        question: str,
        answer: str,
        contexts: List[str],
        ground_truth: str = None
    ) -> Dict[str, float]:
        """Evaluate a single Q&A pair"""
        return self.evaluate(
            questions=[question],
            answers=[answer],
            contexts=[contexts],
            ground_truths=[ground_truth] if ground_truth else None
        )
