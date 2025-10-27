import streamlit as st
import os
from openai import OpenAI
from os import environ

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

import io
from pypdf import PdfReader


client = OpenAI(
    api_key=os.environ["API_KEY"],
    base_url="https://api.ai.it.cornell.edu",
)

# Initialize the text splitter (Spec 3.1)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0,
    add_start_index=True
)

# --- App UI ---
st.title("📝 File Q&A with RAG & ChromaDB")


# Use a sidebar for the file uploader
with st.sidebar:
    st.header("1. Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload one or more documents",
        type=("txt", "md", "pdf"),
        accept_multiple_files=True
    )

    # Only process new uploads (avoid reprocessing on rerun)
    uploaded_names = [f.name for f in uploaded_files] if uploaded_files else []
    prev_uploaded_names = st.session_state.get("processed_file_names", [])

    if uploaded_files and uploaded_names != prev_uploaded_names:
        with st.spinner("Processing documents..."):
            all_texts = []  # to store content from all files

            for uploaded_file in uploaded_files:
                file_content = ""

                # --- Handle PDFs ---
                if uploaded_file.type == "application/pdf":
                    pdf_file = io.BytesIO(uploaded_file.getvalue())
                    reader = PdfReader(pdf_file)
                    text_pages = [
                        page.extract_text() or "" for page in reader.pages]
                    file_content = "\n\n".join(text_pages)

                # --- Handle text or markdown files ---
                elif uploaded_file.type in ["text/plain", "text/markdown"]:
                    file_content = uploaded_file.read().decode("utf-8")

                else:
                    st.error(f"Unsupported file type: {uploaded_file.type}")
                    st.stop()

                # Add file content with filename as a header
                if file_content.strip():
                    all_texts.append(
                        f"## Source: {uploaded_file.name}\n\n{file_content}")

            if not all_texts:
                st.error("No readable text found in uploaded files.")
                st.stop()

            # Combine all texts into one corpus
            combined_text = "\n\n".join(all_texts)

            # 1. Chunk the combined text
            chunks = text_splitter.split_text(combined_text)

            # 2. Create LangChain Document objects
            documents = [Document(page_content=chunk) for chunk in chunks]

            # 3. Create ChromaDB vector store
            vectorstore = Chroma.from_documents(
                documents=documents,
                embedding=OpenAIEmbeddings(
                    model="openai.text-embedding-3-large")
            )

            # 4. Store in session state
            st.session_state.vectorstore = vectorstore
            st.session_state.processed_file_names = uploaded_names

            # 5. Reset chat
            st.session_state.messages = [
                {"role": "assistant",
                    "content": f"I'm ready! Ask me anything about your {len(uploaded_files)} document(s): {', '.join(uploaded_names)}"}
            ]

            st.success("All documents processed and vectorized!")
            st.info("You can now ask questions about the combined content.")
            st.rerun()

# --- 3.3 Conversational Interface ---
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Please upload a document to begin."}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
question = st.chat_input(
    "Ask something about the article",
    disabled="vectorstore" not in st.session_state,
)

# --- 3.2 Retrieval-Augmented Generation (RAG) Pipeline ---
if question and "vectorstore" in st.session_state:

    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)

    vectorstore = st.session_state.vectorstore
    retrieved_docs = vectorstore.similarity_search(question, k=5)
    context = "\n\n---\n\n".join([doc.page_content for doc in retrieved_docs])

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            system_prompt = f"""
            You are an expert Q&A assistant. Your answers must be grounded in the document content.
            Answer the user's question based *only* on the following context.
            If the answer is not in the context, say "I could not find that information in the document."
            
            Context:
            {context}
            """

            history_messages = [
                msg for msg in st.session_state.messages
                if msg["content"] not in [
                    "Please upload a document to begin.",
                    f"I'm ready! Ask me anything about '{st.session_state.get('processed_file_name', '')}'."
                ]
            ]

            messages_for_api = [
                {"role": "system", "content": system_prompt},
                *history_messages
            ]

            stream = client.chat.completions.create(
                model="openai.gpt-4o",
                messages=messages_for_api,
                stream=True
            )

            response = st.write_stream(stream)

    st.session_state.messages.append(
        {"role": "assistant", "content": response})
