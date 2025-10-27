# 📝 File Q&A with RAG & ChromaDB

This Streamlit application allows users to upload one or more text-based documents (`.txt`, `.md`, `.pdf`) and ask natural-language questions about their content.  
It uses **Retrieval-Augmented Generation (RAG)** powered by **ChromaDB** for semantic search and **OpenAI’s GPT model** for grounded question answering.

---

## 🚀 Features

- **Multi-file upload**: Upload one or more `.txt`, `.md`, or `.pdf` documents.  
- **Automatic text extraction**: Extracts and cleans text from uploaded files.  
- **Chunking with LangChain**: Uses `RecursiveCharacterTextSplitter` to split text into smaller chunks for embeddings.  
- **Vector embeddings with ChromaDB**: Converts text chunks into embeddings using `text-embedding-3-large`.  
- **RAG-powered Q&A**: Answers user questions grounded *only* in the document content.  
- **Persistent chat history**: Maintains previous messages via Streamlit session state.  

---

## 🧰 Technologies Used

| Component | Purpose |
|------------|----------|
| **Streamlit** | Interactive web app interface |
| **LangChain** | Text splitting, document representation, embeddings |
| **ChromaDB** | Vector database for similarity search |
| **OpenAI API** | Embeddings and chat completions |
| **pypdf** | PDF text extraction |

## Changes made to initial setup
- Updated `requirements.py` due to conflicting dev container's numpy and pandas versions (removed older pandas version)

---

## 🧭 Getting Started (Forking & Codespaces Setup)

### **Step 1: Fork This Repository**
1. Click the **Fork** button (top right corner of the GitHub page).  
2. This will create a **personal copy** of the repository under your GitHub account.  
3. You can freely commit, push, and experiment on your forked version — your work stays separate from the official class materials.

### **Step 2: Open Your Forked Repo in a Codespace**
1. Navigate to your **forked repository** on GitHub.  
2. Click the green **Code** button.  
3. Select the **Codespaces** tab.  
4. Click **Create Codespace on main** (or your target branch).  
5. Wait a few minutes for the development environment to initialize.  

Once setup completes, you can start running the Streamlit app directly from your browser — no local installation needed!

### **Step 3: Run the streamlit app**
Ensure to put you `API_KEY="your-api-key"` in the `devcontainer.json` and rebuild the container.

Now, In the terminal for the **Codespace** run the following command -   
```
streamlit run chat_with_pdf.py
``` 

###  **Step 4: Chat with the Bot!**
- Utilize the features provided and chat with the pdf/text/md accepting RAG Agent!

---

## ⚙️ Manual Setup (Local Option)

If you’re working locally instead of Codespaces, follow these steps:

### 1️⃣ Prerequisites
- Python 3.9 or higher  
- An OpenAI-compatible API key (configured for `https://api.ai.it.cornell.edu`)  
- Installed dependencies

### 2️⃣ Installation

Clone the repository and install dependencies:
```bash
git clone https://github.com/AtindraJ/INFO-5940-Codespace.git
cd assignment1
pip install -r requirements.txt
```
