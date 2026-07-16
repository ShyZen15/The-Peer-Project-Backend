from App.AI.embeddings.search import EmbeddingSearch
from App.repository.MentorRepo import MentorRepo


class MentorRetriever:

    @staticmethod
    def retrieve(
        embedding: list[float],
        top_k: int = 10
    ) -> list[dict]:

        matches = EmbeddingSearch.searchMentors(
            embedding=embedding,
            top_k=top_k
        )

        recommendations = []

        for match in matches:

            mentor = MentorRepo.getDataByID(
                match["mentor_id"]
            )

            if mentor is None:
                continue

            recommendations.append(
                {
                    "mentor": mentor,
                    "similarity": match["similarity"]
                }
            )

        return recommendations