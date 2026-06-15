from src.repo_indexer import build_repo_index
from src.embeddings import embed_text


def build_vector_index(repo_name):

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

        Content:
        {item['content']}
        """

        vector = embed_text(text)

        vector_index.append({
            **item,
            "embedding": vector
        })

    return vector_index