from langchain_community.vectorstores import Chroma
from app.services.embeddings.embedding_service import get_embedding_model

def create_vector_store(documents):
    embeddings = get_embedding_model()
    db = Chroma.from_documents(documents, embeddings)
    return db