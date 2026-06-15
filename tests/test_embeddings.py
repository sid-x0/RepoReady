from src.embeddings import embed_text

vector = embed_text(
    "Flask web framework"
)

print(type(vector))
print(len(vector))