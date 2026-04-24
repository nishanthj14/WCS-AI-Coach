# 🕺💃 WCS AI Coach

An AI-powered **West Coast Swing coaching assistant** that analyzes dancer-described issues and generates structured, actionable feedback using a **Retrieval-Augmented Generation (RAG)** pipeline.

It behaves like a real dance coach—focused on **diagnosis, causes, cues, and drills**, rather than generic AI advice.

---

## ✨ Key Features

- 🧠 **RAG-based coaching engine** for domain-aware responses  
- 🔍 **FAISS vector search** for fast semantic retrieval of WCS knowledge  
- 🧬 **SentenceTransformer embeddings** for meaning-based similarity  
- 🎯 **Intent-aware reranking** to prioritize relevant dance concepts  
- 🤖 **Ollama LLM integration** (optional local model support)  
- 🧯 **Mock fallback system** for offline/demo reliability  
- 🌐 **React frontend** for user interaction  
- ⚡ **FastAPI backend** for orchestration and inference pipeline  
- 🐳 Fully containerized using Docker Compose  

---

## 🏗️ System Architecture

```
User Input
   ↓
Frontend (React)
   ↓
FastAPI Backend
   ↓
Embedding Model (SentenceTransformer)
   ↓
FAISS Vector Search (WCS Knowledge Base)
   ↓
Intent-aware Reranker
   ↓
Context Builder
   ↓
LLM (Ollama) OR Mock Fallback
   ↓
Structured Coaching Response
   ↓
Frontend Display
```

---

## 🧠 How the RAG Pipeline Works

### 1. User Query
Example:
> "how to be a better follow"

### 2. Embedding
The query is converted into a vector using **SentenceTransformers**.

### 3. FAISS Retrieval
The system retrieves the most semantically similar West Coast Swing concepts from the knowledge base.

### 4. Intent-Aware Reranking
Results are adjusted based on intent signals:
- "follow" → connection, anchor, responsiveness
- "sugar push" → compression, timing
- "whip" → stretch, rotation, slot control

### 5. Context Injection
Relevant WCS knowledge is combined with the user query.

### 6. LLM Generation
An LLM (via Ollama) generates structured coaching feedback.

---

## 🤖 Mock Fallback System

If the LLM is unavailable or Ollama is not running, the system automatically falls back to a deterministic mock generator.

### Why this matters:
- Prevents system failure
- Enables offline demos
- Guarantees consistent API responses

### Example response:
```json
{
  "issue_summary": "Mock analysis of dance issue",
  "likely_causes": [
    "Timing inconsistency",
    "Loss of connection"
  ],
  "coaching_cues": [
    "Slow down weight transfer",
    "Maintain connection"
  ],
  "drills": [
    "Anchor drill",
    "Connection drill"
  ]
}
```

---

## 🧪 Example Interactions

### Input: Better Following
**User:**  
> how to be a better follow

**Output:**
- Issue: Delayed response to lead signals  
- Causes: Premature anchor, weak connection tone  
- Cues: Delay reaction, maintain body tone  
- Drills: Compression response drill, anchor timing drill  

---

### Input: Sugar Push
**User:**  
> sugar push tips

**Output:**
- Issue: Inconsistent compression timing  
- Causes: Pushing instead of receiving energy  
- Cues: Absorb compression, stay elastic  
- Drills: Slot compression drill, anchor timing drill  

---

### Input: Whip Connection
**User:**  
> whip connection issue

**Output:**
- Issue: Loss of stretch during rotation  
- Causes: Collapsing slot, weak connection  
- Cues: Maintain stretch and axis control  
- Drills: Whip rotation drill  

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have:

- Docker (Docker Desktop)
- Docker Compose
- (Optional) Ollama → https://ollama.com

---

### 2. Run the Project

```bash
docker-compose up --build
```

---

### 3. Access the App

- 🌐 Frontend: http://localhost:3000  
- ⚙️ Backend: http://localhost:8000  

---

### 4. Stop Services

```bash
docker-compose down
```

---

## ⚙️ Tech Stack

### Backend
- FastAPI
- FAISS (vector search)
- SentenceTransformers (Embedding model)
- Ollama (optional LLM runtime)

### Frontend
- React

### Infrastructure
- Docker
- Docker Compose

---

## 📚 Knowledge Base Design

The WCS knowledge base is structured around:

- Dance techniques (anchor, connection, compression)
- Common patterns (sugar push, whip, tuck turn)
- Movement principles (slot, stretch, timing)
- Error patterns (disconnects, early anchors, rigidity)

Each entry is embedded and stored in FAISS for semantic retrieval.

---

## 💡 Key Insights

This project shows that:

> Better structured knowledge + retrieval design > larger models

### Major improvements came from:
- Stronger WCS knowledge chunking strategy  
- Intent-aware reranking layer  
- Structured JSON output enforcement  
- Reliable fallback system  
- Clean RAG pipeline design  

---

## 📦 Future Improvements

- [ ] Add multi-turn coaching memory  
- [ ] Add video-based movement tagging  
- [ ] Expand WCS knowledge base (advanced patterns)  
- [ ] Fine-tuned ranking model instead of heuristic reranker  
- [ ] Deploy as cloud SaaS  

---

## 📸 UI Overview

- Clean chat-based coaching interface  
- Structured feedback cards  
- Drill-based actionable output  
- Docker-based reproducible setup  

---

## 🧑‍💻 Author Notes

This system is designed as a **domain-specialized AI coach**, not a generic chatbot. The focus is on:

- Movement correction
- Dance pedagogy structure
- Actionable drills
- Pattern recognition in partner dance

---
