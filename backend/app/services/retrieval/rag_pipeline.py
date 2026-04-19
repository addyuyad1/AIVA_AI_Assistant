from app.services.llm.provider import generate_response
from app.services.retrieval.query_rewriter import rewrite_query
from app.services.retrieval.reranker import rerank_documents
from app.services.retrieval.hybrid_search import hybrid_search

def build_prompt(query: str, docs):
    context = "\n\n".join([doc.page_content[:300] for doc in docs])

    prompt = f"""
You are an AI assistant.

Use ONLY the context below to answer.
If unsure, say "I don't know".

Context:
{context}

Question:
{query}

Answer:
"""
    return prompt



def run_rag_pipeline(query, vector_db, bm25, documents):
    # Step 1: Rewrite
    new_query = rewrite_query(query)

    # Step 2: Hybrid Retrieval
    docs = hybrid_search(new_query, bm25, documents, vector_db)

    # Step 3: Re-rank
    docs = rerank_documents(new_query, docs)

    # Step 4: Build prompt
    prompt = build_prompt(new_query, docs)

    # Step 5: LLM
    answer = generate_response(prompt)

    return {
        "query": query,
        "rewritten_query": new_query,
        "answer": answer,
        "sources": [doc.page_content for doc in docs]
    }