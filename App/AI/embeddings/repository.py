from database import supabase

class EmbeddingRepo():
    @staticmethod
    def createMentorEmbedding(
        mentor_id: str,
        embedding: list[float],
        model: str = "nvidia/llama-nemotron-embed-1b-v2"
    ):
        return (
            supabase
            .table("Mentor Embeddings")
            .insert(
                {
                    "mentor_id": mentor_id,
                    "embedding": embedding,
                    "model": model
                }
            )
            .execute()
        )

    @staticmethod
    def createMenteeEmbedding(
        mentee_id: str,
        embedding: list[float],
        model: str = "nvidia/llama-nemotron-embed-1b-v2"
    ):
        return (
            supabase
            .table("Mentee Embeddings")
            .insert(
                {
                    "mentee_id": mentee_id,
                    "embedding": embedding,
                    "model": model
                }
            )
            .execute()
        )

    @staticmethod
    def updateMentorEmbedding(
        mentor_id: str,
        embedding: list[float],
        model: str = "nvidia/llama-nemotron-embed-1b-v2"
    ):
        return (
            supabase
            .table("Mentor Embeddings")
            .update(
                {
                    "embedding": embedding,
                    "model": model
                }
            )
            .eq("mentor_id", mentor_id)
            .execute()
        )

    @staticmethod
    def updateMenteeEmbedding(
        mentee_id: str,
        embedding: list[float],
        model: str = "nvidia/llama-nemotron-embed-1b-v2"
    ):
        return (
            supabase
            .table("Mentee Embeddings")
            .update(
                {
                    "embedding": embedding,
                    "model": model
                }
            )
            .eq("mentee_id", mentee_id)
            .execute()
        )

    @staticmethod
    def getMentorEmbedding(
        mentor_id: str
    ):
        return (
            supabase
            .table("Mentor Embeddings")
            .select("*")
            .eq("mentor_id", mentor_id)
            .single()
            .execute()
        ).data

    @staticmethod
    def getMenteeEmbedding(
        mentee_id: str
    ):
        return (
            supabase
            .table("Mentee Embeddings")
            .select("*")
            .eq("mentee_id", mentee_id)
            .single()
            .execute()
        ).data

    