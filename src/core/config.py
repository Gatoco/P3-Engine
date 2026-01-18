class Settings:
    PROJECT_NAME: str = "RAG Project 3"
    API_V1_STR: str = "/api/v1"
    
    # Vector DB
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    
    # LLM (Placeholder)
    OPENAI_API_KEY: str | None = None

settings = Settings()
