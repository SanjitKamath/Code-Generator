# 🚀 AI Code Generator with RAG

A sophisticated **Retrieval-Augmented Generation (RAG)** powered code generation tool leveraging **Google Vertex AI Gemini 2.0 Flash** to deliver context-aware code based on best practices and domain knowledge.

---

## 🧠 **Overview**

This application combines the power of modern AI with enterprise-grade vector search to generate high-quality code snippets, complete projects, and technical solutions. It uses a **RAG architecture** to retrieve relevant coding best practices and guidelines before generating responses, ensuring accuracy and contextual relevance.

---

## 🏗️ **Architecture**

The system is composed of the following key components:

- **`main.py`** – FastAPI web server with RESTful endpoints  
- **`generator.py`** – Core engine that integrates semantic retrieval with AI generation  
- **`build_knowledge_base.py`** – Tool to build and maintain the FAISS vector knowledge base  
- **Web Interface** – A clean and responsive frontend for user interaction

---

## 🧰 **Technologies Used**

### 🖥️ **Core Technologies**
- **Python 3.8+** – Main programming language  
- **FastAPI** – Web framework for API creation  
- **Uvicorn** – ASGI server for running FastAPI apps  

### 🤖 **AI & Machine Learning**
- **Google Vertex AI** – Managed platform for deploying AI models  
- **Gemini 2.0 Flash Lite** – Multimodal model for fast, code-aware generation  
- **Text Embedding Model (`text-embedding-005`)** – For semantic document retrieval  

### 📦 **Vector Search & Retrieval**
- **FAISS** – High-performance vector similarity search  
- **NumPy** – For numerical vector computations  

### ☁️ **Cloud Services**
- **Google Cloud Storage (GCS)** – Storage for knowledge base assets  
- **Google Cloud AI Platform** – Model hosting and management  

### 🌐 **Frontend Technologies**
- **HTML5 / CSS3** – Structure and styling  
- **JavaScript (ES6+)** – Frontend interactivity  
- **Responsive Design** – Optimized for mobile and desktop devices  

---

## ✨ **Features**

### 💡 **Intelligent Code Generation**
- Context-aware code suggestions  
- Multi-language output  
- Integrated security and best practices  

### 🔍 **Advanced Retrieval System**
- FAISS-based semantic search engine  
- Curated and extendable knowledge base  
- Efficient processing for large document sets  

### 💻 **Web Interface**
- Intuitive, clean UI  
- Real-time response display  
- Ready-to-copy code formatting  

### 🏢 **Enterprise Features**
- Scalable deployment architecture  
- Built-in logging and monitoring  
- Configurable via environment variables  

---

## ⚡ **Quick Start**

### ✅ **Prerequisites**
- Python 3.8 or higher  
- Google Cloud Platform account with **Vertex AI** enabled  
- Google Cloud Storage bucket (optional, for persistence)

### 📥 **Installation Steps**

1. **Clone the repository**

   git clone https://github.com/your-org/ai-code-generator.git
   cd ai-code-generator


2. **Install dependencies**


   pip install -r requirements.txt


3. **Configure environment**
   Create a `.env` file in the root directory:

   VERTEX_PROJECT_ID=your-gcp-project-id
   VERTEX_LOCATION=us-central1
   GCS_BUCKET_NAME=your-gcs-bucket-name


4. **Build the knowledge base**


   python build_knowledge_base.py


5. **Start the application**

   python main.py

Access the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)


## 📁 **Project Structure**

```
ai-code-generator/
├── build_knowledge_base.py # Builds FAISS index from documents
├── generator.py # RAG engine: embeddings + generation
├── main.py # FastAPI app entry point
├── templates/ # HTML templates
├── static/ # CSS & JS assets
├── .env # Environment variables
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```
