import os
from src.embeddings.chroma_manager import get_chroma_client, get_collection
from src.embeddings.embedder import get_text_embedding

def search_docs(query: str, top_k: int = 3):
    """
    Search for documents in ChromaDB that are semantically similar to the given query.
    
    Args:
        query (str): The user's search query (e.g., "risk clauses in contracts")
        top_k (int): Number of most relevant documents to return

    Returns:
        list of dicts: Each dict contains file path and document snippet
    """
    if not query.strip():
        return [{"error": "Query cannot be empty"}]

    print(f"\n🔍 Searching for: '{query}'")

    client = get_chroma_client()
    collection = get_collection(client)
    
    # Convert query into embedding
    query_embedding = get_text_embedding(query)
    
    # Query the database
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    matched_docs = []
    print(f"\nTop {top_k} matching documents:\n")

    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        snippet = doc[:300].replace("\n", " ")
        print(f"📄 {meta['source']}")
        print(f"➡️  {snippet}...\n")
        matched_docs.append({
            "file_path": meta['source'],
            "preview": snippet
        })
    
    return matched_docs


# -------------------------------
# Quick test
# -------------------------------
if __name__ == "__main__":
    query = "risk clauses in employment contracts"
    results = search_docs(query, top_k=3)

    print("\n=== Final Search Results ===")
    for r in results:
        print(f"📁 File: {r['file_path']}")
        print(f"🧠 Preview: {r['preview'][:150]}...\n")
