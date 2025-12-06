import chromadb
from sentence_transformers import SentenceTransformer

# Initialize ChromaDB client and collection
client = chromadb.Client()
collection = client.create_collection("user_memories")

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def store_user_memory(user_id, memory_type, memory_text):
    """
    Store a memory with a type (e.g., 'preference', 'trip', 'query', 'recommendation')
    """
    embedding = embedder.encode(memory_text).tolist()
    doc = f"[{memory_type}] {memory_text}"
    mem_id = f"{user_id}_{memory_type}_{abs(hash(memory_text))}"
    collection.add(
        embeddings=[embedding],
        documents=[doc],
        ids=[mem_id]
    )
    print(f"Memory stored! Type: {memory_type}")

def search_user_memories(query, memory_type=None, n_results=3):
    """
    Search for similar memories, optionally filtering by type.
    """
    query_embedding = embedder.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    docs = results['documents'][0]
    if memory_type:
        docs = [d for d in docs if d.startswith(f"[{memory_type}]")]
    return docs

if __name__ == "__main__":
    user_id = "user_001"
    # Store different types of memories
    store_user_memory(user_id, "preference", "User likes food tours and spicy cuisine.")
    store_user_memory(user_id, "trip", "Visited Lahore for 3 days in 2023.")
    store_user_memory(user_id, "query", "Best places to visit in Islamabad?")
    store_user_memory(user_id, "recommendation", "Recommended Hunza for nature lovers.")

    print("\nSearching for similar memories (all types)...")
    found = search_user_memories("food in Lahore")
    for mem in found:
        print(" -", mem)

    print("\nSearching for trip memories only...")
    found = search_user_memories("visited Lahore", memory_type="trip")
    for mem in found:
        print(" -", mem) 