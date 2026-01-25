# Define la interfaz (puerto) para cualquier servicio de generación de embeddings.
from abc import ABC, abstractmethod
from typing import List
from src.domain.models.chunk import Chunk

class EmbeddingPort(ABC):
    @abstractmethod
    def generate_embeddings(self, chunks: List[Chunk]) -> List[Chunk]:
        """Genera y asigna embeddings a una lista de chunks."""
        pass