from database import supabase

class EmbeddingSearch:

    @staticmethod
    def searchMentors(
        embedding: list[float],
        top_k: int = 10,
    ) -> list[dict]:
        
        response = (
            supabase
            .rpc(
                "match_mentors",
                {
                    "query_embedding": embedding,
                    "match_count": top_k
                }
            )
            .execute()
        )

        return response.data
    
    @staticmethod
    def searchMentees(
        embedding: list[float],
        top_k: int = 10
    ) -> list[dict]:
        response = (
            supabase
            .rpc(
                "match_mentees",
                {
                    "query_embedding": embedding,
                    "match_count": top_k
                }
            )
            .execute()
        )

        return response.data