from App.AI.embeddings.service import EmbeddingService
from App.AI.retrieval.mentor_retriever import MentorRetriever

from App.schemas.mentees import MenteesRegistration

class MentorMatchingPipeline:

    @staticmethod
    def recommend(
        mentee: MenteesRegistration,
        top_k: int = 10
    ):
        
        embedding = EmbeddingService.mentee_embedding(
            mentee
        )

        recommendations = MentorRetriever.retrieve(
            embedding=embedding,
            top_k=top_k
        )

        return recommendations