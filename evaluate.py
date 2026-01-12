from memory import store_memory, retrieve

store_memory("User likes finance")
store_memory("User prefers short answers")

hits = retrieve("What should I read?")
print("Retrieved memory:", hits)
