import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # LLM
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    LLM_MODEL = os.getenv("LLM_MODEL")

    # Embeddings
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

    # Redis
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = os.getenv("REDIS_PORT")

    # DB
    DATABASE_URL = os.getenv("DATABASE_URL")

    # App
    DEBUG = os.getenv("DEBUG", "False") == "True"

settings = Settings()