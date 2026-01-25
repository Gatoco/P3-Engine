# Define el modelo Pydantic para la respuesta del sistema RAG.
from pydantic import BaseModel
from typing import List, Dict, Any

class Source(BaseModel):
    document_id: str
    chunk_id: str
    content: str
    metadata: Dict[str, Any]

class Response(BaseModel):
    answer: str
    sources: List[Source]