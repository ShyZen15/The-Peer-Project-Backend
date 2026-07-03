from fastapi import APIRouter
from App.schemas.mentor import MentorRegistration
from App.repository.MenteeRepo import MenteeRepo

router = APIRouter(
    prefix="/mentor",
    tags=["Mentor"]
)

@router.post("/")
async def register_mentor(
    mentor: MentorRegistration
): 
    result = MenteeRepo.createData(
        mentor.model_dump(mode="json")
    )

    return {
        "success": True,
        "mentor": result.data
    }