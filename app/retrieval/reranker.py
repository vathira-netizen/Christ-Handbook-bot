from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, docs):

    pairs = [
        (query, doc.page_content)
        for doc in docs
    ]

    scores = model.predict(pairs)

    scored_docs = list(zip(scores, docs))

    ranked = sorted(
        scored_docs,
        key=lambda x: x[0],
        reverse=True
    )

    return [doc for score, doc in ranked]