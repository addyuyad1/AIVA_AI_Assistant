from app.services.llm.provider import generate_response

def rerank_documents(query, docs):
    scored_docs = []

    for doc in docs:
        prompt = f"""
Rate the relevance of this document to the query from 1 to 10.

Query: {query}

Document: {doc.page_content}

Score:
"""
        score = generate_response(prompt)

        try:
            score = int(score.strip())
        except:
            score = 5

        scored_docs.append((doc, score))

    scored_docs.sort(key=lambda x: x[1], reverse=True)

    return [doc for doc, _ in scored_docs[:3]]