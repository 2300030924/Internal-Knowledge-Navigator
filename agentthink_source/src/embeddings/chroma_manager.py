import os
import chromadb
from chromadb.config import Settings
from src.embeddings.embedder import get_text_embedding
from src.utils.file_utils import list_files_in_folder, read_file, clean_text

# -------------------------------
# Initialize ChromaDB client
# -------------------------------
from chromadb import PersistentClient

def get_chroma_client():
    """Initialize and return a persistent Chroma client (new API)."""
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    db_path = os.path.join(base_dir, "chroma_db")

    # Create a persistent Chroma client using the modern API
    client = PersistentClient(path=db_path)
    return client


# -------------------------------
# Create or get collection
# -------------------------------
def get_collection(client, name="documents"):
    """Return or create a Chroma collection."""
    collection = client.get_or_create_collection(name=name)
    return collection

# -------------------------------
# Ingest all documents into Chroma
# -------------------------------
def ingest_documents(folder_path):
    """Read all documents, generate embeddings, and store them in ChromaDB."""
    client = get_chroma_client()
    collection = get_collection(client)
    files = list_files_in_folder(folder_path)

    print(f"📂 Found {len(files)} documents to ingest...")

    for file_path in files:
        text = read_file(file_path)
        if not text.strip():
            print(f"[WARN] Empty file skipped: {file_path}")
            continue

        clean = clean_text(text)
        embedding = get_text_embedding(clean)

        collection.add(
            documents=[clean],
            embeddings=[embedding],
            metadatas=[{"source": file_path}],
            ids=[os.path.basename(file_path)]
        )

        print(f"✅ Ingested: {os.path.basename(file_path)}")

   
    print("\n💾 All documents stored in ChromaDB successfully!")

# -------------------------------
# Semantic search
# -------------------------------
def search_documents(query, top_k=3):
    """Search for similar documents using embeddings."""
    client = get_chroma_client()
    collection = get_collection(client)

    query_embedding = get_text_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    print("\n🔍 Top Matching Documents:")
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        print(f"📄 {meta['source']}")
        print(f"➡️  {doc[:300]}...\n")

    return results


# -------------------------------
# Quick test
# -------------------------------
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    folder = os.path.join(base_dir, "data")

    # Ingest documents (run once)
    ingest_documents(folder)

    # Try searching for a query
    search_documents("risk clauses in contracts")
