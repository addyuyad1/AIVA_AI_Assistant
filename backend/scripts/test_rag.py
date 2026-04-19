from app.ingestion.loaders import load_text
from app.ingestion.chunking import chunk_documents
from app.services.retrieval.base import create_vector_store
from app.services.retrieval.hybrid_search import get_retriever
from app.services.retrieval.rag_pipeline import run_rag_pipeline

# Load docs
docs = load_text("sample.txt")

# Chunk
chunks = chunk_documents(docs)

# Vector DB
db = create_vector_store(chunks)

# Retriever
retriever = get_retriever(db)

# Query
query = "What is RAG?"

# Run RAG
result = run_rag_pipeline(query, retriever)

print("\n===== ANSWER =====\n")
print(result["answer"])

print("\n===== SOURCES =====\n")
for s in result["sources"]:
    print("-", s)