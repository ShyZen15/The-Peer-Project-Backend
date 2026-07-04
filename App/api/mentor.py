from fastapi import APIRouter
from App.schemas.mentor import MentorRegistration
from App.repository.MentorRepo import MentorRepo

router = APIRouter(
    prefix="/mentor",
    tags=["Mentor"]
)

@router.post("/")
async def register_mentor(
    mentor: MentorRegistration
): 
    result = MentorRepo.createData(
        mentor.model_dump(mode="json")
    )

    return {
        "success": True,
        "mentor": result.data
    }

@router.get("/")
async def get_mentor_all():
    result = MentorRepo.getAll()
    return {
        "success": True,
        "mentor": result
    }

@router.get("/{discord_id}")
async def get_mentor_id(discord_id: str):
    result = MentorRepo.getDataByID(discord_id)
    return{
        "success": True,
        "mentor": result
    }

@router.put("/{discord_id}")
async def update_mentor_more(discord_id: str, data:dict):
    result = MentorRepo.updateData(discord_id, data)
    return{
        "success": True,
        "mentor": result.data
    }

@router.put("/{discord_id}")
async def update_mentor_one_field(discord_id: str, data, field:str):
    result = MentorRepo.updateDataField(discord_id, data, field)
    return{
        "success": True,
        "mentor": result.data
    }

@router.delete("/{discord_id}")
async def delete_mentor_id(discord_id: str):
    result = MentorRepo.deleteData(discord_id)
    return{
        "success": True,
        "mentor": result.data
    }

@router.get("/")
async def getTotal():
    return MentorRepo.getCount()
