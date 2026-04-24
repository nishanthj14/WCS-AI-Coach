import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

with open("app/data/wcs_knowledge.json") as f:
    docs = json.load(f)

texts = [d["content"] for d in docs]

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)


def rerank(query, chunks):
    q = query.lower()

    weights = {
        "follow": ["connection", "anchor", "compression", "response"],
        "lead": ["frame", "compression", "redirect"],
        "sugar push": ["compression", "slot", "anchor"],
        "whip": ["rotation", "redirect", "slot"]
    }

    scored = []

    for c in chunks:
        text = c["content"].lower()
        score = 0

        for key, boosts in weights.items():
            if key in q:
                for b in boosts:
                    if b in text:
                        score += 1

        scored.append((score, c))

    scored.sort(key=lambda x: x[0], reverse=True)

    return [c for _, c in scored]


def retrieve_context(query, top_k=3):
    q = model.encode([query]).astype("float32")
    distances, indices = index.search(q, top_k)

    print("\nQUERY:", query)
    print("DISTANCES:", distances)
    print("RAW RESULTS:")
    for i in indices[0]:
        print("-", docs[i]["topic"])

    # 🔥 STEP 1: FAISS retrieval
    retrieved = [docs[i] for i in indices[0]]

    # 🔥 STEP 2: rerank (THIS WAS MISSING BEFORE)
    reranked = rerank(query, retrieved)

    print("RERANKED RESULTS:")
    for r in reranked:
        print("-", r["topic"])

    return reranked