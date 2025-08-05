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
# Setting Up Google Cloud Console for Your RAG-Based Code Generator

This guide walks you through the step-by-step process to configure your Google Cloud Platform (GCP) environment for deploying and running a Retrieval-Augmented Generation (RAG) based code generator.

---

## 1. **Create a GCP Project**
- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Click on the project dropdown (top left) and select **"NEW PROJECT."**
- Give it a unique name and remember the **Project ID** (you’ll use this in your `.env` file and code).

---

## 2. **Enable Required APIs**
- Navigate to **APIs & Services > Library** within your project.
- Enable the following APIs:
  - **Vertex AI API**
  - **Cloud Storage API**
  - **IAM Service Account Credentials API**

---

## 3. **Set Up Vertex AI**
- Go to **Vertex AI > Overview** in the sidebar.
- Click **Enable Vertex AI API** if prompted.
- In **Model Garden**, make sure required models are accessible in your region (e.g., `us-central1`):
  - "Gemini 2.0 Flash"
  - "text-embedding-005"

---

## 4. **Create and Configure a Cloud Storage Bucket**
- Go to **Cloud Storage > Buckets**.
- Click **CREATE**.
- Provide a globally unique bucket name, like: `your-project-rag-bucket`.
- Set the region to match your Vertex AI region (e.g., `us-central1`).
- This bucket will be used to store the FAISS index and ingested text documents.

---

## 5. **Create a Service Account and Grant Permissions**
- Navigate to **IAM & Admin > Service Accounts**.
- Click **CREATE SERVICE ACCOUNT**.
- Give it a name like `vertex-ai-rag-service`.
- Assign the following roles:
  - **Vertex AI User**
  - **Storage Object Admin**
- After creation, go to the "KEYS" tab:
  - Click **ADD KEY > Create new key > JSON**
  - Download and securely store the JSON key file (needed for local development).

---

## 6. **Set Environment Variables (.env)**

Create a `.env` file in your project root with the following:

```env
VERTEX_PROJECT_ID=your-gcp-project-id
VERTEX_LOCATION=us-central1
GCS_BUCKET_NAME=your-bucket-name
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account-key.json
```

Ensure `/path/to/your/service-account-key.json` is the absolute path to your downloaded key.

> ✅ For cloud deployment: Use Secret Manager instead of environment variables, and never hardcode credentials.

---

## 7. **(Optional) Check Vertex AI Quotas & Region Alignment**
- Go to **Vertex AI > Quotas** to verify available limits.
- Confirm all resources (models, bucket, etc.) reside in the same region for optimal performance.

---

## 8. **Enable Billing**
- Make sure billing is enabled on your GCP project.
- Note: Vertex AI and Cloud Storage **are not free**. Charges depend on usage.

---

## ✅ After Completing These Steps
You are ready to:
- Run your code generator locally using authenticated API calls.
- Build the FAISS knowledge base.
- Deploy to a cloud service if desired.

---

## 🔁 Summary of Steps

1. ✅ Create GCP Project  
2. ✅ Enable Vertex AI & Storage APIs  
3. ✅ Set Up Vertex AI  
4. ✅ Create Cloud Storage Bucket  
5. ✅ Create Service Account with permissions  
6. ✅ Set Environment Variables  
7. ✅ Ensure same region setup  
8. ✅ Enable Billing  

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
