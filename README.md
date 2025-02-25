---

# INFO-5940

Welcome to the John Kowalczyk Project 1 repository! This guide will help you set up the development environment using **Docker** in **VS Code**, configure the **OpenAI API key**.

---

## Prerequisites  

Before starting, ensure you have the following installed on your system:  

- [Docker](https://www.docker.com/get-started) (Ensure Docker Desktop is running)  
- [VS Code](https://code.visualstudio.com/)  
- Python 3.11
- [VS Code Remote - Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)  
- [Git](https://git-scm.com/)  
- OpenAI API Key  

---

## Setup Guide  

### 1️: Clone the Repository  

Open a terminal and run:  

```bash
git clone https://github.com/johnkowalczyk/Info5940Project1.git
cd Info5940Project1
```

### 2. Configure OpenAI API Key  
Set the API Key in `.env` (Recommended)  

1. Inside the project folder, create a `.env` file:  

   ```bash
   touch .env
   ```

2. Add your API key and base URL:  

   ```plaintext
   OPENAI_API_KEY=your-api-key-here
   OPENAI_BASE_URL=https://api.ai.it.cornell.edu/
   TZ=America/New_York
   ```
### Run the program:
1. Open the terminal
2. Start the container:  
```bash
docker-compose up --build
```
3. Now, after built, go to the localhost port 8501: 
```bash
http://0.0.0.0:8501/
```
---

### Modifications to Docker and Devcontainer:
1. Added the following libraries to help with the RAG application with Langchain FAISS
```bash
langchain = "^0.2.15"
langchain_core = "^0.2.15"
langchain-openai = "^0.1.23"
PyPdf2 = "^3.0.1"
streamlit = "^1.0"
langchain-community = "^0.2.15"
faiss-cpu = "1.10.0"
```
2. Allowed the program to run on port 8501, by adding code in the Dockerfile to expose the port, and in docker-compose.yml to include the port. 


### Feature Explanation
1. File Upload:
Allows users to upload multiple files with extensions .txt, .md, and .pdf using st.file_uploader.
Extracts text from PDF files using the python library PyPDF2 and the program reads text or markdown files directly.

2. Chatbot Interface:
Provides a chat input box using st.chat_input for users to enter questions to prompt the LLM (with or without rag functinality). 
The program maintains the conversation history using st.session_state.

3. Text Preprocessing:
The code uses RecursiveCharacterTextSplitter to split documents into chunks.

4. Retrieval:
Generates text embeddings using OpenAIEmbeddings with the text-embedding-3-large model.
The vectors for the documents in a FAISS vector store from langchain for similarity search.
Starts a retriever that returns the top 5 most relevant document chunks for any query for the user.

5. RAG Workflow:
When a user asks the interface a question, the system retrieves the top 5 most relavant document chunks if files have been uploaded.
The retrieved content is provided as context to the OpenAI GPT-4o-mini model to generate responses.
If no files are uploaded, the chatbot responds without additional context.
