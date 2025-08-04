import os
import numpy as np
import faiss
import vertexai
from vertexai.language_models import TextEmbeddingModel

# === CONFIG ===
PROJECT_ID = "true-energy-464318-g4"
LOCATION = "us-central1"
USE_GCS = False  # Set to True if saving to GCS
BUCKET_NAME = "your-bucket-name"
INDEX_PREFIX = "rag-data"  # folder/prefix within bucket

# === STEP 1: Initialize Vertex AI ===
vertexai.init(project=PROJECT_ID, location=LOCATION)

# === STEP 2: Define Instruction Documents ===
# === STEP 2: Define Instruction Documents for the Code Generator ===
documents = [
    " Understand the user's intent: identify the primary goal, preferred language, type of app (CLI, GUI, web), constraints (performance, simplicity, security), and domain-specific needs.",
    " Write clean, modular code if asked by the user: use clear variable and function names, small reusable functions, proper docstrings, and follow the style guide (e.g., PEP8, ESLint).",
    " Validate inputs and handle edge cases: check types, formats, missing values, and handle errors (e.g., file not found, API failure) with try/except blocks.",
    " Follow security best practices: never hardcode secrets, sanitize user input, avoid eval(), and use HTTPS and token-based auth for web apps.",
    " Add usage documentation: include inline comments",
    " Format output code clearly: return copy-pastable, well-formatted code blocks, with consistent indentation, no debug prints, and clear file names if split.",
    " Make code reusable and extensible: modularize logic, use config variables, and comment areas that are likely to change or expand.",
    " Apply post-generation quality checks: lint the code, remove unused code, and ensure syntax correctness. Include at least one test or example.",
    " Adapt to unclear prompts: ask clarifying questions when necessary, and suggest safer or more efficient alternatives if the user’s request is suboptimal."
]


# === STEP 3: Save Local Copy of Documents ===
np.save("texts.npy", documents)

# === STEP 4: Get Vertex AI Embeddings ===
print("⏳ Getting embeddings from Vertex AI...")
embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-005")

embeddings = [
    embedding_model.get_embeddings([doc])[0].values
    for doc in documents
]
embeddings_np = np.array(embeddings, dtype="float32")

# === STEP 5: Build FAISS Index ===
dimension = embeddings_np.shape[1]  # Should be 768
index = faiss.IndexFlatL2(dimension)
index.add(embeddings_np)
faiss.write_index(index, "faiss_index.index")

print("✅ Local FAISS index and text documents saved.")

# === STEP 6 (Optional): Upload to GCS ===