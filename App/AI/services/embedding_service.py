from App.AI.embeddings.formatter import ProfileFormatter
from App.AI.embeddings.encoder import EmbeddingEncoder
from App.AI.embeddings.repository import EmbeddingRepo

from App.repository.MentorRepo import MentorRepo
from App.repository.MenteeRepo import MenteeRepo

class EmbeddingService:

    @staticmethod
    def embed_mentor(mentor):
        profile = ProfileFormatter.mentor_profile(mentor)
        embedding = EmbeddingEncoder.encode(profile)
        EmbeddingRepo.createMentorEmbedding(
            mentor.discord_id,
            embedding, 
            "nvidia/llama-nemotron-embed-1b-v2"
        )
        
    @staticmethod
    def embed_mentee(mentee):
        profile = ProfileFormatter.mentee_profile(mentee)
        embedding = EmbeddingEncoder.encode(profile)
        EmbeddingRepo.createMentorEmbedding(
            mentee.discord_id,
            embedding, 
            "nvidia/llama-nemotron-embed-1b-v2"
        )

    @staticmethod
    def updateMentorEmbedding(mentor):

        profile = ProfileFormatter.mentor_profile(mentor)

        embedding = EmbeddingEncoder.encode(profile)

        return EmbeddingRepo.updateMentorEmbedding(
            mentor_id=mentor.discord_id,
            embedding=embedding
        )


    @staticmethod
    def updateMenteeEmbedding(mentee):

        profile = ProfileFormatter.mentee_profile(mentee)

        embedding = EmbeddingEncoder.encode(profile)

        return EmbeddingRepo.updateMenteeEmbedding(
            mentee_id=mentee.discord_id,
            embedding=embedding
        )


    @staticmethod
    def getMentorEmbedding(mentor_id: str):

        return EmbeddingRepo.getMentorEmbedding(mentor_id)


    @staticmethod
    def getMenteeEmbedding(mentee_id: str):

        return EmbeddingRepo.getMenteeEmbedding(mentee_id)