from src.utils.chunking import chunk_text
from typing import List, Dict, Any

def prepare_text_for_embedding(text: str, chunk_size: int = 500, overlap: int = 100) -> List[Dict[str, Any]]:
    """
    Prepara el texto para la generación de embeddings, dividiéndolo en fragmentos (chunks) optimizados.
    
    Esta función actúa como un paso intermedio crucial antes de enviar los datos al modelo de embeddings
    y posteriormente a la base de datos vectorial (Qdrant). Asegura que el texto respete los límites
    de contexto del modelo y mantenga la coherencia semántica mediante solapamiento.

    Args:
        text (str): El texto completo a procesar.
        chunk_size (int, opcional): Tamaño máximo de cada fragmento. 
                                    Se recomienda un valor compatible con el modelo de embedding (ej. 512 tokens -> aprox 1500-2000 caracteres, 
                                    pero ajustamos conservadoramente a 500 para pruebas o modelos más pequeños).
        overlap (int, opcional): Cantidad de caracteres que se solapan entre chunks consecutivos.
                                 Ayuda a preservar el contexto en los límites de corte.

    Returns:
        List[Dict[str, Any]]: Lista de diccionarios, donde cada uno contiene el texto del chunk y metadatos básicos.
                              Formato: [{'chunk_index': 0, 'text': '...'}, ...]
    """
    
    # 1. Validación básica de entrada
    if not text or not isinstance(text, str):
        print("Advertencia: Se recibió un texto vacío o inválido.")
        return []

    # 2. Utilizar la utilidad de chunking existente
    # La función chunk_text ya maneja la lógica de ventana deslizante y overlap.
    # Aquí adaptamos o envolvemos esa lógica para el dominio de embeddings.
    chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)

    # 3. Post-procesamiento (opcional, por ahora pasamos directo)
    # En el futuro, aquí podríamos agregar metadatos adicionales necesarios para Qdrant,
    # como IDs generados, timestamps, o referencias al documento original.
    
    # 4. Retornar la lista estructurada
    return chunks
