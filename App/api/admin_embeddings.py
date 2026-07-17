from fastapi import APIRouter, Depends, HTTPException

from App.auth.dependencies import get_current_admin 
from App.repository.MentorRepo import MentorRepo
from App.repository.MenteeRepo import MenteeRepo
from App.AI.services.embedding_service import EmbeddingService

router = APIRouter(
    prefix="/admin/embeddings",
    tags=["Admin Embeddings"]
)


@router.post("/mentor/{mentor_id}")
async def generate_mentor_embedding(
    mentor_id: str,
    current_admin=Depends(get_current_admin)
):

    mentor = MentorRepo.getDataByIDSingle(mentor_id)

    if mentor is None:
        raise HTTPException(
            status_code=404,
            detail="Mentor not found"
        )

    EmbeddingService.embed_mentor(mentor)

    return {
       "message": "Mentor embedding created successfully."
    }

@router.post("/mentee/{mentee_id}")
async def generate_mentee_embedding(
    mentee_id: str,
    current_admin=Depends(get_current_admin)
):

    mentee = MenteeRepo.getDataByIDSingle(mentee_id)

    if mentee is None:
        raise HTTPException(
            status_code=404,
            detail="Mentor not found"
        )

    EmbeddingService.embed_mentee(mentee)

    return {
        "message": "Mentor embedding created successfully."
    }