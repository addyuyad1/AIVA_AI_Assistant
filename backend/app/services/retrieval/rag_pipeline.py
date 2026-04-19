from app.services.llm.provider import generate_response

def build_prompt(query: str, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI assistant.

Use ONLY the context below to answer the question.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}

Answer:
"""
    return prompt


def run_rag_pipeline(query: str, retriever):
    docs = retriever.invoke(query)

    prompt = build_prompt(query, docs)

    response = generate_response(prompt)

    return {
        "answer": response,
        "sources": [doc.page_content for doc in docs]
    }