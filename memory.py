from embeddings import embed
from vector_store import VectorStore

store = VectorStore()

def store_memory(text):
    e = embed([text])[0]
    store.add([e],[text])

def retrieve(query):
    q = embed([query])[0]
    return store.search(q, k=5)
