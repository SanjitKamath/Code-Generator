```markdown
# AI Code Generator with RAG

A sophisticated **Retrieval-Augmented Generation (RAG)** powered code generation application that leverages Google's Vertex AI Gemini 2.0 Flash model to provide intelligent, context-aware code generation based on best practices and domain-specific knowledge.

## Overview

This application combines the power of modern AI with enterprise-grade vector search to generate high-quality code snippets, complete projects, and technical solutions. The system uses a RAG architecture to retrieve relevant coding best practices and guidelines before generating responses, ensuring more accurate and contextually appropriate code generation.

## Architecture

The system consists of several key components:

- **FastAPI Web Application** (`main.py`): RESTful API server with web interface
- **RAG Code Generator** (`generator.py`): Core engine that combines vector search with AI generation
- **Knowledge Base Builder** (`build_knowledge_base.py`): Utility to create and maintain the vector knowledge base
- **Web Interface**: Clean, responsive frontend for user interactions

## Technologies Used

### Core Technologies
- **Python 3.8+**: Primary programming language
- **FastAPI**: High-performance, modern web framework for building APIs
- **Uvicorn**: Lightning-fast ASGI server for serving the FastAPI application

### AI & Machine Learning
- **Google Vertex AI**: Enterprise AI platform for model hosting and management
- **Gemini 2.0 Flash Lite**: Latest generation multimodal AI model for code generation
- **Text Embedding Model (text-embedding-005)**: Advanced embedding model for semantic search

### Vector Search & Retrieval
- **FAISS (Facebook AI Similarity Search)**: High-performance vector similarity search library
- **NumPy**: Numerical computing library for vector operations

### Cloud Services
- **Google Cloud Storage**: Scalable object storage for knowledge base persistence
- **Google Cloud AI Platform**: Managed AI services and model deployment

### Frontend Technologies
- **HTML5/CSS3**: Modern web standards for user interface
- **JavaScript (ES6+)**: Interactive frontend functionality
- **Responsive Design**: Mobile-friendly user experience

## Features

### Intelligent Code Generation
- **Context-Aware Generation**: Uses RAG to provide relevant coding context
- **Multi-Language Support**: Generates code in various programming languages
- **Best Practices Integration**: Built-in knowledge of coding standards and patterns
- **Security-First Approach**: Follows security best practices in generated code

### Advanced Retrieval System
- **Semantic Search**: FAISS-powered vector similarity search
- **Knowledge Base**: Curated collection of coding guidelines and best practices
- **Scalable Architecture**: Handles large-scale document collections efficiently

### Web Interface
- **Clean UI**: Intuitive and user-friendly interface
- **Real-time Generation**: Instant feedback and code generation
- **Copy-Paste Friendly**: Well-formatted, ready-to-use code output

### Enterprise Features
- **Scalable Deployment**: Cloud-native architecture
- **Logging & Monitoring**: Comprehensive application logging
- **Error Handling**: Robust error management and user feedback
- **Configuration Management**: Environment-based configuration

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Cloud Platform account with Vertex AI enabled
- Google Cloud Storage bucket (optional, for knowledge base storage)

### Installation

1. **Clone the repository**
    ```
    git clone 
    cd ai-code-generator
    ```

2. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```

3. **Set up environment variables**
    Create a `.env` file in the root directory:
    ```
    VERTEX_PROJECT_ID=your-gcp-project-id
    VERTEX_LOCATION=us-central1
    GCS_BUCKET_NAME=your-gcs-bucket-name
    ```

4. **Build the knowledge base**
    ```
    python build_knowledge_base.py
    ```

5. **Run the application**
    ```
    python main.py
    ```

The application will be available at `http://127.0.0.1:8000`

## Project Structure

```
ai-code-generator/
├── main.py                  # FastAPI application entry point
├── generator.py             # RAG-based code generation engine
├── build_knowledge_base.py  # Knowledge base creation utility
├── requirements.txt         # Python dependencies
├── static/
│   ├── style.css            # Application styles
│   └── script.js            # Frontend JavaScript
├── templates/
│   └── index.html           # Main application template
└── README.md                # This file
```

## 🔧 Configuration

### Environment Variables
- `VERTEX_PROJECT_ID`: Your Google Cloud Project ID
- `VERTEX_LOCATION`: Vertex AI location (default: us-central1)
- `GCS_BUCKET_NAME`: Google Cloud Storage bucket for knowledge base
- `KMP_DUPLICATE_LIB_OK`: Set to "TRUE" to handle library conflicts

### Knowledge Base Configuration
The knowledge base can be customized by modifying the `documents` array in `build_knowledge_base.py`. Add your own coding guidelines, best practices, or domain-specific knowledge to improve generation quality.

## Usage Examples

### Basic Code Generation
1. Navigate to the web interface
2. Enter a natural language description of your coding needs
3. Click "Generate" to receive AI-generated code
4. Copy and use the generated code in your projects


## 🔒 Security Considerations

- **API Key Management**: Never commit API keys to version control
- **Input Validation**: All user inputs are validated and sanitized
- **Secure Defaults**: Application follows security-first principles
- **HTTPS Ready**: Designed for secure deployment with HTTPS

## 🚀 Deployment

### Local Development
```
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### Production Deployment
For production deployments, consider:
- Using a production ASGI server like Gunicorn
- Setting up proper logging and monitoring
- Implementing rate limiting and authentication
- Using environment-specific configuration


## Acknowledgments

- **Google Vertex AI** for providing state-of-the-art AI models
- **Facebook AI Research** for the FAISS library
- **FastAPI** community for the excellent web framework
- **Meta AI** for RAG research and methodologies




[4] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/80699761/c095638b-77ce-4b5e-9335-49cf1e085354/index.html
[5] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/80699761/be9249a8-d454-4c6a-90b0-3f1c3c890835/script.js
[6] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/80699761/d26cfdd3-f1d6-4725-81c9-7afe3f7e8c61/style.css
