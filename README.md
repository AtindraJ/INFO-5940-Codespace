# 📝 File Q&A with RAG & ChromaDB

This Streamlit application allows users to upload one or more text-based documents (`.txt`, `.md`, `.pdf`) and ask natural-language questions about their content.  
It uses **Retrieval-Augmented Generation (RAG)** powered by a persistent **ChromaDB** for semantic search and **OpenAI’s GPT model** for grounded question answering.

---

## 🚀 Features

- **Multi-file upload**: Upload one or more `.txt`, `.md`, or `.pdf` documents.
- **Automatic text extraction**: Extracts and cleans text from uploaded files.
- **Chunking with LangChain**: Uses `RecursiveCharacterTextSplitter` to break text into manageable pieces for embedding.
- **Vector embeddings with ChromaDB**: Converts text chunks into embeddings using OpenAI's `text-embedding-3-large`.
- **RAG-powered Q&A**: Uses similarity search and GPT to answer questions *only* from uploaded document content.
- **Persistent chat context**: Maintains conversation history in `st.session_state`.

---

## 🧰 Technologies Used

| Component | Purpose |
|------------|----------|
| **Streamlit** | Web UI framework |
| **LangChain** | Text splitting, document handling, and embedding abstraction |
| **ChromaDB** | Local vector database for document retrieval |
| **OpenAI API** | Embeddings and chat completions |
| **pypdf** | PDF text extraction |

---

## ⚙️ Setup Instructions
### Changes made to initial setup
- Updated `requirements.py` due to conflicting dev container's numpy and pandas versions

### 1️⃣ Prerequisites

- Python 3.9+  
- An OpenAI-compatible API key (configured for `https://api.ai.it.cornell.edu`)  
- Installed dependencies (see below)

### 2️⃣ Installation

Clone the repository and install dependencies:
```bash
git clone <your-repo-url>
cd <your-repo-folder>
pip install -r requirements.txt
