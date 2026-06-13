import numpy as np
from embeddings import embed_text



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

    for item in vector_index:

        score = cosine_similarity(
            query_vector,
            item["embedding"]
        )

        results.append(
            (score, item)
        )

    results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return results[:top_k]