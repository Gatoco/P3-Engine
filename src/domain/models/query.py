# Define el modelo Pydantic para una consulta de usuario.
from pydantic import BaseModel
from typing import Optional, Dict, Any

class Query(BaseModel):
    question: str
    session_id: Optional[str] = None
    filters: Optional[Dict[str, Any]] = None