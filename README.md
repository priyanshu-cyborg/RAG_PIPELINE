# 📚 RAG Mini Project – Retrieval Augmented Generation (Beginner Friendly)

This repository contains a **mini project on Retrieval-Augmented Generation (RAG)** created to clearly understand the **core concepts behind RAG pipelines**, embeddings, vector search, and context-based answer generation.

This project is intentionally kept **simple and modular** so that beginners can easily grasp how real-world RAG systems work.

---

## 🚀 What is RAG?
**Retrieval-Augmented Generation (RAG)** is a technique that improves the accuracy of language model outputs by **retrieving relevant information from an external knowledge base** before generating a response.

Instead of relying only on a model’s internal knowledge, RAG follows this pipeline:

```
Query → Retrieval → Context Augmentation → Answer Generation
```

---

## 🎯 Project Objective
The goal of this project is to:
- Understand how **text is converted into vector embeddings**
- Learn how **similarity search** works using vector databases
- Implement a **basic RAG pipeline** from scratch
- Reduce hallucinations by grounding responses in retrieved knowledge

---

## 🧠 Project Architecture

```
User Question
     ↓
Sentence Embedding (Sentence-BERT)
     ↓
Similarity Search (FAISS)
     ↓
Relevant Documents
     ↓
Context-based Answer Generation
```

---

## 🛠️ Tech Stack Used
- **Python**
- **Sentence-BERT** – for text embeddings
- **FAISS** – for vector similarity search
- **NumPy** – numerical operations

---

## 📁 Project Structure

```
rag_mini_project/
│
├── data.py          # Sample knowledge base documents
├── embed_store.py   # Embedding generation + FAISS index
├── rag_pipeline.py  # Retrieval + generation logic
└── main.py          # User interaction
```

---

## 📘 Step-by-Step Explanation

### 1️⃣ Data Preparation (`data.py`)
Stores a small set of sample documents that act as the **external knowledge base**.

---

### 2️⃣ Embeddings & Vector Store (`embed_store.py`)
- Uses **Sentence-BERT** to convert documents into vectors
- Stores vectors in **FAISS**
- Performs similarity search using Euclidean distance

Key concepts learned:
- Text → Vector conversion
- Vector indexing
- Nearest neighbor search

---

### 3️⃣ RAG Pipeline (`rag_pipeline.py`)
- Retrieves the most relevant documents based on user query
- Combines retrieved content as context
- Generates an answer using augmented context

This demonstrates the **Retrieve → Augment → Generate** workflow.

---

### 4️⃣ User Interaction (`main.py`)
Allows users to ask questions and receive answers based on retrieved documents.

---

## 🧪 Example Usage

```
Ask a question: What is RAG?

Answer:
RAG stands for Retrieval Augmented Generation.
RAG combines information retrieval with text generation.
```

---

## 📚 Key Concepts Covered

| Concept | Description |
|------|-------------|
| Embeddings | Numerical representation of text |
| Similarity Search | Finding nearest vectors |
| FAISS | Vector database for fast retrieval |
| RAG Pipeline | Retrieval + Generation |
| NLP Fundamentals | Context-aware answering |

---

## 🌱 Future Enhancements
- Add **PDF document ingestion**
- Integrate **OpenAI / LLaMA models** for generation
- Use **cosine similarity** instead of L2 distance
- Build a **Streamlit UI**
- Add **chat history memory**
- Upgrade to **Chroma / Pinecone** vector DB

---

## 🏁 Conclusion
This mini project provides a **strong foundational understanding of RAG systems** and prepares the ground for building advanced applications like:
- AI chatbots
- Document Q&A systems
- Knowledge assistants

---

## ✨ Author
**Priyanshu Sharma**  
MCA (Big Data Analytics) | AI & NLP Enthusiast  

🔗 Feel free to connect on LinkedIn and explore the project!
https://www.linkedin.com/in/priyanshu-sharma-70a835320/
---

⭐ If you found this helpful, don’t forget to star the repository!

