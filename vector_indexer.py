from repo_indexer import build_repo_index
from embeddings import embed_text


def build_vector_index(repo_name):
    index = build_repo_index(repo_name)

    vector_index = []

    for item in index:

        text = (
            item["file"]
            + " "
            + " ".join(item["classes"])
            + " "
            + " ".join(item["functions"])
        )

        vector = embed_text(text)

        vector_index.append({
            **item,
            "embedding": vector
        })

    return vector_index