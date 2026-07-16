from App.AI.embeddings.encoder import EmbeddingEncoder
from App.AI.embeddings.formatter import ProfileFormatter

from App.schemas.mentor import MentorRegistration
from App.schemas.mentees import MenteesRegistration


class EmbeddingService:
    @staticmethod
    def mentor_embedding(mentor:MentorRegistration) -> list[float]:
        profile = ProfileFormatter.mentor_profile(mentor)

        embedding = EmbeddingEncoder.encode(profile)

        return embedding
    
    @staticmethod
    def mentee_embedding(mentee: MenteesRegistration) -> list[float]:
        profile = ProfileFormatter.mentee_profile(mentee)
        embedding = EmbeddingEncoder.encode(profile)
        return embedding
