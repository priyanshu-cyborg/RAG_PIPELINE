from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from data import documents

model = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = model.encode(documents)
doc_embeddings = np.array(doc_embeddings, dtype=np.float32)

dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

def retrieve_docs(query, top_k=2):
    query_embeddings = model.encode([query])
    query_embeddings = np.array(query_embeddings, dtype=np.float32)

    top_k = max(1, min(top_k, len(documents)))

    distances, indices = index.search(query_embeddings, top_k)
    return [documents[i] for i in indices[0] if i != -1]