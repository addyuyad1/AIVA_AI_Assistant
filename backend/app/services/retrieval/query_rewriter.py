from app.services.llm.provider import generate_response

def rewrite_query(query: str):
    prompt = f"""
Rewrite the following query to make it more clear and detailed for document retrieval:

Query: {query}

Rewritten Query:
"""
    return generate_response(prompt)