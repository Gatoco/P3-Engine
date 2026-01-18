# P3-Engine (RAG System)

## Descripción General
Este repositorio contiene la implementación de referencia para el Proyecto 3: Sistema de Recuperación Aumentada por Generación (RAG). El objetivo es desarrollar una arquitectura escalable para la ingesta, indexación y recuperación de información a partir de documentos no estructurados (PDFs, Markdown, Texto), permitiendo consultas en lenguaje natural mediante Modelos de Lenguaje Grande (LLMs).

El diseño prioriza la modularidad, la separación de responsabilidades y la extensibilidad para futuros componentes de evaluación y re-ranking.

## Especificaciones Técnicas

### Arquitectura Propuesta
- **Ingesta**: Pipeline ETL para extracción de texto y metadatos.
- **Embedding**: Generación de vectores densos (Modelo: *TBD* - e.g., OpenAI text-embedding-3, HuggingFace Local).
- **Almacenamiento Vectorial**: Base de datos vectorial persistente (Qdrant/Chroma).
- **Recuperación**: Búsqueda semántica con estrategia de HNSW.
- **Generación**: Integración con LLM vía API (OpenAI/Anthropic) o inferencia local (Ollama).
- **API**: Interface RESTful para exposición de endpoints (FastAPI).

### Requerimientos del Sistema
- Runtime: Python 3.11+
- Containerización: Docker & Docker Compose
- Gestión de Dependencias: Poetry / Pip

### Estructura del Proyecto
El proyecto sigue una arquitectura hexagonal simplificada:

```
rag/
├── src/
│   ├── api/            # Controladores y endpoints REST
│   ├── core/           # Configuración global y logging
│   ├── domain/         # Modelos de dominio y esquemas
│   ├── services/       # Lógica de negocio (Ingestion, Retrieval, Chat)
│   └── adapters/       # Interfaces con servicios externos (VectorDB, LLM)
├── tests/              # Pruebas unitarias e integración
├── notebooks/          # Experimentación y evaluación
├── docker/             # Configuración de despliegue
└── scripts/            # Utilidades de mantenimiento
```

## Dependencias (Preliminar)
Las versiones específicas están pendientes de definición final, pero el stack base incluye:
- `fastapi`
- `uvicorn`
- `pydantic`
- `langchain` / `llama-index`
- `qdrant-client` / `chromadb`
- `tiktoken`
- `python-dotenv`

## Despliegue Local
El entorno de desarrollo se orquesta mediante Docker Compose.

```bash
docker-compose up -d --build
```
