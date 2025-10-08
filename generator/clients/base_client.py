# ============================================
# FILE: generator/clients/base_client.py
# ============================================
from abc import ABC, abstractmethod


class BaseLLMClient(ABC):
    """Base interface for LLM clients"""
    
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generates content based on the prompt.
        
        Args:
            prompt: Input text for the model
            
        Returns:
            Model response as a string
        """
        pass