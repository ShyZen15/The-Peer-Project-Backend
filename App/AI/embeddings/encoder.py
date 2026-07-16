from langchain_huggingface import HuggingFaceEmbeddings

class EmbeddingEncoder:

    _embedding_model = HuggingFaceEmbeddings(
        model_name="nvidia/llama-nemotron-embed-1b-v2",
        model_kwargs={
            "device": "cuda",
            "trust_remote_code": True
        },
        encode_kwargs={
            "normalize_embeddings": True
        }

    )

    @classmethod
    def encode(cls, text: str) -> list[float]:
        return cls._embedding_model.embed_query(text)

