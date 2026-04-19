from rank_bm25 import BM25Okapi

def create_bm25_index(documents):
    corpus = [doc.page_content.split() for doc in documents]
    return BM25Okapi(corpus), documents


def hybrid_search(query, bm25, documents, vector_db, k=3):
    # BM25
    tokenized_query = query.split()
    bm25_scores = bm25.get_scores(tokenized_query)

    bm25_results = sorted(
        zip(documents, bm25_scores),
        key=lambda x: x[1],
        reverse=True
    )[:k]

    bm25_docs = [doc for doc, _ in bm25_results]

    # Vector search
    vector_docs = vector_db.similarity_search(query, k=k)

    seen = set()
    combined = []

    for doc in bm25_docs + vector_docs:
        content = doc.page_content  # use text as unique key
        if content not in seen:
            seen.add(content)
            combined.append(doc)

    return combined