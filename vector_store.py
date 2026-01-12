import numpy as np

class VectorStore:
    def __init__(self):
        self.vectors = []
        self.texts = []

    def add(self, embeddings, texts):
        for e,t in zip(embeddings,texts):
            self.vectors.append(e)
            self.texts.append(t)

    def search(self, query, k=5):
        sims = np.dot(self.vectors, query)
        idx = np.argsort(sims)[-k:][::-1]
        return [self.texts[i] for i in idx]
