from fastapi import APIRouter
from App.schemas.mentees import MenteesRegistration
from App.repository.MenteeRepo import MenteeRepo

router = APIRouter(
    prefix="/mentee",
    tags=["Mentee"]
)

@router.post("/")
async def register_mentor(
    mentees: MenteesRegistration
): 
    result = MenteeRepo.createData(
        mentees.model_dump(mode="json")
    )

    return {
        "success": True,
        "mentor": result.data
    }