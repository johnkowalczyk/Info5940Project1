import streamlit as st
from openai import OpenAI
from os import environ
import PyPDF2
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain_community.vectorstores import FAISS

st.title("Info 5940 Project 1: Rag Chatbot")
uploaded_files = st.file_uploader("Upload articles", type=("txt", "md", "pdf"), accept_multiple_files=True)

question = st.chat_input(
    "Ask me anything!",
)

client = OpenAI(api_key=environ['OPENAI_API_KEY'])

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Ask me anything!"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

uploaded_files = None #helps for no context LLM

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_type = uploaded_file.name.split('.')[-1].lower()
        if file_type == "pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            file_content_arr = [page.extract_text() for page in reader.pages]
            file_content = "".join(file_content_arr)
        else:
            file_content = uploaded_file.read().decode("utf-8")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
        )
        documents = [Document(page_content=file_content)]
        chunks = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings(
                model="openai.text-embedding-3-large",
                api_key=environ["OPENAI_API_KEY"]
            )
        vectorstore = FAISS.from_documents(chunks, embeddings)
        retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)

    if uploaded_files:
        retrieved_docs = retriever.invoke(question)
        print([f"Doc {i}:\n{retrieved_docs[i]}" for i in range(len(retrieved_docs))])
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)
        relevant_text = format_docs(retrieved_docs)
    else:
        relevant_text = "No relevant text."
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="openai.gpt-4o-mini", 
        messages=[
            {"role": "system", "content": "You are an AI assistant. Answer using the context provided."},
            {"role": "system", "content": f"Context:\n{relevant_text}\n"},
            *st.session_state.messages
        ],
            stream=True
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
