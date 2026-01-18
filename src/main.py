from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import settings

app = FastAPI(
    title="RAG Project 3 API",
    description="API for Retrieval-Augmented Generation System",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json", 
    docs_url="/api/v1/docs"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "rag-api"}
