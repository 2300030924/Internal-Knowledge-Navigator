# Internal Knowledge Navigator

An AI-powered system that enables semantic search and intelligent navigation
over internal documents using Retrieval-Augmented Generation (RAG).

This project is designed to help organizations quickly find relevant
information from internal knowledge bases such as HR policies, legal documents,
and technical files.

---

## 🚀 Key Features
- Semantic search over internal documents
- Context-aware responses using LLMs
- Document ingestion and embedding pipeline
- Modular, extensible architecture
- Supports structured and unstructured documents

---

## 🧠 System Architecture (High Level)

1. Documents are ingested and preprocessed  
2. Text is converted into vector embeddings  
3. Embeddings are stored for fast similarity search  
4. User queries are embedded and matched semantically  
5. Retrieved context is passed to the LLM for response generation  

This follows a **Retrieval-Augmented Generation (RAG)** approach.

---

## 🛠 Tech Stack
- **Language:** Python  
- **LLM / API:** Gemini  
- **Embeddings:** Sentence Transformers  
- **Vector Store:** ChromaDB  
- **Backend:** Python modules  
- **Utilities:** JSON, file-based ingestion  

---

## 📂 Project Structure
