from encoder import EmbeddingEncoder
embedding = EmbeddingEncoder.encode("Hello World")
print(len(embedding))

# print("1")

# from langchain_huggingface import HuggingFaceEmbeddings

# print("2")

# model = HuggingFaceEmbeddings(
#     model_name="nvidia/llama-nemotron-embed-1b-v2",
#     model_kwargs={
#         "device":"cuda",
#         "trust_remote_code":True
#     },
#     encode_kwargs={
#         "normalize_embeddings":True
#     }
# )

# print("3")

# print("4")

# embedding = model.embed_query("Hello World")

# print("5")