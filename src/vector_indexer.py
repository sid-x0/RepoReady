from src.repo_indexer import build_repo_index
from src.embeddings import embed_text

from src.cache_utils import (
    load_cache,
    save_cache
)


def build_vector_index(repo_name):

    cached = load_cache(repo_name)

    if cached is not None:

        print("\nLoaded index from cache.")

        return cached

    print("\nBuilding vector index...")

    index = build_repo_index(repo_name)

    vector_index = []

    for item in index:

        filename = item["file"].split("/")[-1]

        text = f"""
        Filename:
        {filename}

        Full Path:
        {item['file']}

        Type:
        {item['type']}

        Classes:
        {' '.join(item.get('classes', []))}

        Functions:
        {' '.join(item.get('functions', []))}

        Content:
        {item['content'][:1000]}
        """
        vector = embed_text(text)

        vector_index.append({
            **item,
            "embedding": vector
        })

    save_cache(
        repo_name,
        vector_index
    )

    print("\nIndex cached successfully.")

    return vector_index