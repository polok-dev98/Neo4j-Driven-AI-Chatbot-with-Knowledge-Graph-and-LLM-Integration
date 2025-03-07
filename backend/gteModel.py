import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

def embedding_model_download(folder):
    os.makedirs(folder, exist_ok=True)
    hf_token = os.getenv("HF_TOKEN")
    sentence_model_name = "thenlper/gte-large"
    
    # Load and save the SentenceTransformer model
    sentence_model = SentenceTransformer(sentence_model_name, use_auth_token=hf_token)
    sentence_model.save(folder)
    
    print(f"SentenceTransformer model saved to {folder}")

embedding_model_download("GeneralTextEmbeddingModel")
