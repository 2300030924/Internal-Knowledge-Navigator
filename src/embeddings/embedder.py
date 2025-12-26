# src/embeddings/embedder.py
from sentence_transformers import SentenceTransformer

# Load the local embedding model (downloaded once, then cached)
model = SentenceTransformer("D:/Projects/Aiml/Models/all-MiniLM-L6-v2")


def get_text_embedding(text: str):
    """
    Converts text into numerical embeddings (vectors) using a local model.
    Works offline and doesn't consume Gemini API tokens.
    """
    if not text.strip():
        return []
    
    # Generate the embedding vector
    embedding = model.encode(text)
    
    # Convert numpy array to Python list
    return embedding.tolist()

# -------------------------------
# Function 2: Quick test
# -------------------------------
if __name__ == "__main__":
    sample_text = """
    Employment Contract - This document defines responsibilities,
    compensation, and risk-sharing between employer and employee.
    """
    print("Generating local embedding for sample text...\n")
    embedding = get_text_embedding(sample_text)
    print("Embedding length:", len(embedding))
    print("First 10 values:", embedding[:10])
