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
cd INFO-5940
```

---
### 2️. Open in VS Code with Docker  

1. Open **VS Code**, navigate to the `INFO-5940` folder.  
2. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) and search for:  
   ```
   Remote-Containers: Reopen in Container
   ```
3. Select this option. VS Code will build and open the project inside the container.  

**Note:** If you don’t see this option, ensure that the **Remote - Containers** extension is installed.  

---

### 3️. Configure OpenAI API Key  
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

3. Restart the container:  

   ```bash
   docker-compose up --build
   ```

Now, after built, go to the localhost port 8501: 
```bash
http://0.0.0.0:8501/
```
---

Modifications to Docker and Devcontainer:
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