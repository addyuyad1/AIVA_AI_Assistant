from app.ingestion.loaders import load_text
from app.ingestion.chunking import chunk_documents
from app.services.retrieval.base import create_vector_store
from app.services.retrieval.hybrid_search import get_retriever

docs = load_text("backend\sample.txt")
chunks = chunk_documents(docs)

db = create_vector_store(chunks)
retriever = get_retriever(db)

results = retriever.invoke("What is this document about?")

for r in results:
    print(r.page_content)