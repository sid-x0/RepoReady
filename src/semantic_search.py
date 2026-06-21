import numpy as np
from src.embeddings import embed_text
import re


def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)

    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0

    return dot_product / (norm_vec1 * norm_vec2)


def semantic_search(vector_index, query, top_k=5):

    query_vector = embed_text(query)

    results = []

    query_words = query.lower().split()
    
    symbols = re.findall(
        r"[A-Za-z_][A-Za-z0-9_]*",
        query
    )

    for item in vector_index:

        score = cosine_similarity(
            query_vector,
            item["embedding"]
        )

        file_path = item["file"].lower()
        filename = item["file"].split("/")[-1].lower()

        content = item.get(
            "content",
            ""
        ).lower()
        
        if item["type"] == "code":
            score += 0.5

        for word in query_words:

            if len(word) <= 3:
                continue

            if word in filename:
                score += 0.50

            elif word in file_path:
                score += 0.20

            if word in content:
                score += 0.40
                
        for symbol in symbols:

            if len(symbol) <= 3:
                continue

            if symbol.lower() in content:
                score += 5.0

        results.append(
            (score, item)
        )

    results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    print("\nTop 10 Rankings:")

    for score, item in results[:10]:
        print(
            round(score, 3),
            item["file"]
        )


    return results[:top_k]