
# chunking_example.py

def chunk_text(text: str, chunk_size: int = 200, overlap: int = 50):
    """
    Divide un texto dado en fragmentos (chunks) más pequeños basados en el número de caracteres,
    permitiendo un solapamiento (overlap) entre ellos para mantener el contexto.

    Esta función es fundamental para procesos de RAG (Retrieval Augmented Generation),
    ya que permite procesar textos largos que exceden la ventana de contexto de los modelos de lenguaje.

    Args:
        text (str): El texto original completo que se desea dividir.
        chunk_size (int, opcional): El tamaño máximo de cada fragmento eñ caracteres.
                                    Por defecto es 200.
        overlap (int, opcional): El número de caracteres que se repetirán entre el final de un chunk
                                 y el inicio del siguiente. Esto es crucial para no cortar frases
                                 o ideas a la mitad sin contexto. Por defecto es 50.

    Returns:
        list[dict]: Una lista de diccionarios, donde cada diccionario representa un chunk y contiene:
            - 'chunk_index': El índice secuencial del fragmento (0, 1, 2, ...).
            - 'text': El contenido textual del fragmento.
    """
    # Validación inicial: si el texto está vacío o es None, retornamos una lista vacía
    if not text:
        return []

    chunks = []
    
    # Calculamos el 'step' o paso de avance. 
    # El paso es el tamaño del chunk menos el overlap.
    # Ejemplo: Si chunk_size=200 y overlap=50, avanzamos 150 caracteres cada vez.
    # Usamos max(..., 1) para asegurar que el paso sea al menos 1 y evitar bucles infinitos.
    step = max(chunk_size - overlap, 1)

    # Iteramos a través del texto usando range con el 'step' calculado.
    # 'start' tomará valores como 0, 150, 300, etc.
    for index, start in enumerate(range(0, len(text), step)):
        # Extraemos el fragmento desde la posición 'start' hasta 'start + chunk_size'.
        # Python maneja automáticamente si el índice final excede la longitud del texto.
        chunk = text[start:start + chunk_size]

        # Agregamos el chunk procesado a nuestra lista de resultados
        chunks.append({
            "chunk_index": index,
            "text": chunk
        })

    return chunks


if __name__ == "__main__":
    # Texto de prueba (realista)
    text = """
    La inteligencia artificial moderna permite construir sistemas que
    combinan modelos de lenguaje con bases de conocimiento externas.
    Los sistemas RAG utilizan embeddings para recuperar información
    relevante antes de generar una respuesta.
    """

    # Ejecutar chunking
    chunks = chunk_text(
        text=text,
        chunk_size=200,
        overlap=50
    )

    # Mostrar resultados
    print(f"Total de chunks: {len(chunks)}\n")

    for chunk in chunks:
        print(f"Chunk {chunk['chunk_index']}:")
        print(chunk["text"].strip())
        print("-" * 50)
