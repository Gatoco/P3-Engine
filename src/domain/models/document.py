# Define el modelo de dominio para un Documento, representando el dato de entrada.
from pydantic import BaseModel, Field
from typing import Dict, Any
import uuid

class Document(BaseModel):
    """
    Representa una unidad de contenido que ha sido cargada en el sistema.
    
    Atributos:
        id (str): Identificador único para el documento, generado como UUID.
        name (str): Nombre del archivo o fuente del documento (ej. "politica_vacaciones.pdf").
        content (str): Contenido textual completo del documento.
        metadata (Dict[str, Any]): Diccionario flexible para metadatos adicionales 
                                     (ej. {"source": "URL", "author": "John Doe"}).
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)