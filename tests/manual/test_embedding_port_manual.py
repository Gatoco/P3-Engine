import sys
import os

# Ajustamos el path para que encuentre 'src' desde 'tests/manual'
# Asumiendo que se corre desde la raíz del proyecto o desde la misma carpeta,
# necesitamos llegar a la raíz del proyecto (dos niveles arriba de tests/manual)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
if project_root not in sys.path:
    sys.path.append(project_root)

from src.domain.ports.embedding_port import prepare_text_for_embedding

def test_embedding_preparation():
    text = """
    La inteligencia artificial generativa ha revolucionado la forma en que interactuamos con la información.
    Los sistemas RAG (Retrieval-Augmented Generation) combinan la potencia de los modelos de lenguaje
    con la precisión de las bases de datos vectoriales.
    
    Qdrant es una base de datos vectorial eficiente que permite búsquedas de similitud a gran escala.
    Al dividir el texto en chunks con solapamiento, aseguramos que el contexto no se pierda entre fragmentos,
    lo cual es crucial para obtener embeddings de alta calidad y respuestas precisas.
    """
    
    print("Iniciando prueba de prepare_text_for_embedding...")
    chunks = prepare_text_for_embedding(text, chunk_size=100, overlap=20)
    
    print(f"\nTexto original longitud: {len(text)}")
    print(f"Chunks generados: {len(chunks)}\n")
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i}: len={len(chunk['text'])}")
        print(f"'{chunk['text']}'")
        print("-" * 30)
        
    if len(chunks) > 0:
        print("\n✅ Prueba exitosa: Se generaron chunks correctamente.")
    else:
        print("\n❌ Prueba fallida: No se generaron chunks.")

if __name__ == "__main__":
    test_embedding_preparation()
