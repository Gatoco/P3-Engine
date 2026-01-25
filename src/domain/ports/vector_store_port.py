# Define la interfaz (puerto) para cualquier base de datos vectorial.
from abc import ABC, abstractmethod
from typing import List
from src.domain.models.chunk import Chunk

class VectorStorePort(ABC):
    @abstractmethod
    def upsert(self, chunks: List[Chunk]) -> None:
        """Inserta o actualiza chunks en la base de datos vectorial."""
        pass

    @abstractmethod
    def query(self, query_embedding: List[float], top_k: int = 5) -> List[Chunk]:
        """Realiza una búsqueda de similitud y devuelve los chunks más relevantes."""
        pass

    @abstractmethod
    def delete(self, document_id: str) -> None:
        """Elimina todos los chunks asociados a un document_id."""
        pass