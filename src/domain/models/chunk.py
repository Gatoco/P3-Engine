# Define el modelo de dominio para un Chunk, un fragmento de un documento.
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List

class Chunk(BaseModel):
    """
    Representa un trozo (chunk) de un Documento. Es la unidad atómica
    que se utiliza para la generación de embeddings y la búsqueda de similitud.
    
    Atributos:
        id (str): Identificador único para el chunk.
        document_id (str): ID del documento al que pertenece este chunk.
        content (str): El texto del chunk.
        embedding (Optional[List[float]]): El vector numérico (embedding) que representa el contenido del chunk.
        metadata (Dict[str, Any]): Metadatos heredados del documento o específicos del chunk 
                                     (ej. número de página, sección).
    """
    id: str = Field(default_factory=lambda: f"chunk_{uuid.uuid4()}")
    document_id: str
    content: str
    embedding: Optional[List[float]] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)