import os
import re
import sys
import numpy as np
import faiss
import logging
import tempfile
from vertexai import init
from vertexai.preview.generative_models import GenerativeModel, Part
from vertexai.language_models import TextEmbeddingModel
from google.cloud import storage

# Logging setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler("app.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

class CodeGenerator:
    def __init__(self):
        # Initialize Vertex AI
        init(
            project=os.getenv("VERTEX_PROJECT_ID", "true-energy-464318-g4"),
            location=os.getenv("VERTEX_LOCATION", "us-central1")
        )
        logger.info("Vertex AI initialized.")

        try:
            self.code_model = GenerativeModel("gemini-2.0-flash-lite")
            logger.info("Loaded Gemini 2.0 Flash Lite model.")
        except Exception as e:
            logger.error("Failed to load generative model.")
            raise

        try:
            self.embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-005")
            logger.info("Loaded embedding model.")
        except Exception as e:
            logger.error("Failed to load embedding model.")
            raise

        self.index = None
        self.texts = []
        try:
            self.gcs_client = storage.Client()
            self.load_from_gcs()
            logger.info("FAISS index and texts loaded from GCS.")
        except Exception as e:
            logger.error("Error loading from GCS.")
            raise

    def load_from_gcs(self):
        bucket_name = os.getenv("GCS_BUCKET_NAME")
        if not bucket_name:
            raise ValueError("GCS_BUCKET_NAME not set in environment.")

        bucket = self.gcs_client.bucket(bucket_name)
        tmp_dir = tempfile.gettempdir()

        index_path = os.path.join(tmp_dir, "faiss_index.index")
        bucket.blob("knowledge_base/faiss_index.index").download_to_filename(index_path)
        self.index = faiss.read_index(index_path)

        texts_path = os.path.join(tmp_dir, "texts.npy")
        bucket.blob("knowledge_base/texts.npy").download_to_filename(texts_path)
        self.texts = np.load(texts_path, allow_pickle=True)

    def get_embedding(self, text: str) -> list:
        embeddings = self.embedding_model.get_embeddings([text])
        return embeddings[0].values

    def retrieve_context(self, query: str, k=3) -> str:
        query_embedding = np.array(self.get_embedding(query), dtype="float32").reshape(1, -1)
        logger.info(f"Query embedding shape: {query_embedding.shape}, index dim: {self.index.d}")

        if query_embedding.shape[1] != self.index.d:
            raise ValueError(f"Embedding dim {query_embedding.shape[1]} != index dim {self.index.d}")

        distances, indices = self.index.search(query_embedding, k)
        return "\n\n".join([self.texts[i] for i in indices[0]])

    def generate_code(self, query: str) -> str:
        try:
            context = self.retrieve_context(query)
        except Exception as e:
            logger.error("Context retrieval failed.")
            return f"Error generating code: Context error - {str(e)}"

        prompt = f"""
        [Company Context]
        {context}

        [User Request]
        {query}

        [Instructions]
        1. Understands the user goal
        2. Selects the best language and libraries
        3. Generates minimal but complete project structure
        4. Applies best coding practices
        5. Handles input validation and edge cases
        6. Documents usage
        7. Ensures security
        8. Formats code cleanly
        9. Adds room for customization
        10. Responds only with code unless the user asks for explanations.
        """

        try:
            response = self.code_model.generate_content(prompt)
            return self._clean_code_output(response.text)
        except Exception as e:
            logger.error(f"Code generation failed: {str(e)}")
            return f"Error generating code: {str(e)}"

    def _clean_code_output(self, text: str) -> str:
        code_blocks = re.findall(r'```[^\n]*\n(.*?)\n```', text, re.DOTALL)
        return code_blocks[0] if code_blocks else text
