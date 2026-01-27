# P3-Engine (RAG System)

## Descripción General
Este repositorio contiene la implementación de referencia para el Proyecto 3: Sistema de Recuperación Aumentada por Generación (RAG). El objetivo es desarrollar una arquitectura escalable para la ingesta, indexación y recuperación de información a partir de documentos no estructurados (PDFs, Markdown, Texto), permitiendo consultas en lenguaje natural mediante Modelos de Lenguaje Grande (LLMs).

El diseño prioriza la modularidad, la separación de responsabilidades y la extensibilidad para futuros componentes de evaluación y re-ranking.

## Especificaciones Técnicas

### Arquitectura Propuesta
- **Ingesta**: Pipeline ETL para extracción de texto y metadatos.
- **Embedding**: Generación de vectores densos (Locales con `sentence-transformers` o APIs).
- **Almacenamiento Vectorial**: Base de datos vectorial persistente (**Qdrant**).
- **Recuperación**: Búsqueda semántica optimizada.
- **Generación**: Integración con LLM vía API (Google Vertex AI / Gemini) o inferencia local.
- **API**: Interface RESTful para exposición de endpoints (**FastAPI**).

### Requerimientos del Sistema
- Runtime: Python 3.11+
- Containerización: Docker & Docker Compose
- Gestión de Dependencias: Pip (requirements.txt)

### Estructura del Proyecto
El proyecto sigue una arquitectura modular organizada en `src`:

```
rag/
├── docker/
│   ├── docker-compose.yml
│   └── Dockerfile
├── notebooks/
│   ├── chunking_tests.ipynb
│   ├── embedding_quality.ipynb
│   └── retrieval_eval.ipynb
├── scripts/
│   └── ingest_cli.py
├── src/
│   ├── adapters/
│   │   ├── embeddings/
│   │   │   ├── openai_embeddings.py
│   │   │   └── sentence_transformer.py
│   │   ├── llm/
│   │   │   ├── ollama_llm.py
│   │   │   └── openai_llm.py
│   │   ├── loaders/
│   │   │   ├── markdown_loader.py
│   │   │   ├── pdf_loader.py
│   │   │   └── text_loader.py
│   │   └── vector_store/
│   │       └── qdrant_store.py
│   ├── api/
│   │   ├── routes/
│   │   │   ├── chat.py
│   │   │   ├── health.py
│   │   │   └── ingest.py
│   │   └── main.py
│   ├── core/
│   │   ├── config.py
│   │   ├── logging.py
│   │   └── settings.py
│   ├── domain/
│   │   ├── models/
│   │   │   ├── chunk.py
│   │   │   ├── document.py
│   │   │   ├── query.py
│   │   │   └── response.py
│   │   └── ports/
│   │       ├── embedding_port.py
│   │       ├── llm_port.py
│   │       └── vector_store_port.py
│   ├── services/
│   │   ├── ingestion_service.py
│   │   ├── rag_service.py
│   │   ├── rerank_service.py
│   │   └── retrieval_service.py
│   └── utils/
│       ├── chunking.py
│       └── token_counter.py
├── tests/
├── .gitignore
├── LICENSE
├── README.md
├── requirements-dev.txt
└── requirements.txt
```

## Dependencias
El stack tecnológico actual incluye las siguientes librerías clave (ver `requirements.txt`):

### Core & API
- `fastapi`: Framework web moderno y rápido.
- `uvicorn`: Servidor ASGI.
- `pydantic[settings]`: Validación de datos y gestión de configuración.
- `loguru`: Sistema de logging mejorado.

### RAG & AI
- `langchain`: Orquestación de flujos de LLM.
- `google-cloud-aiplatform`: Cliente para Google Vertex AI (Gemini).
- `sentence-transformers`: Modelos de embedding locales.
- `qdrant-client`: Cliente para base de datos vectorial Qdrant.
- `pypdf`: Extracción de texto desde PDFs.
- `unstructured[md]`: Procesamiento de documentos Markdown.

### Utilities
- `typer`: Creación de interfaces de línea de comandos (CLI).

## Despliegue Local
El entorno de desarrollo se puede orquestar mediante Docker Compose (ubicado en la carpeta `docker/`).

```bash
# Navegar a la carpeta de docker y levantar servicios
cd docker
docker-compose up -d --build
```

Alternativamente, para desarrollo local sin docker:

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor (ejemplo)
uvicorn src.api.main:app --reload
```
