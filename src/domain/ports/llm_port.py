# Define la interfaz (puerto) para cualquier Modelo de Lenguaje Grande (LLM).
from abc import ABC, abstractmethod

class LLMPort(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Genera una respuesta de texto a partir de un prompt."""
        pass