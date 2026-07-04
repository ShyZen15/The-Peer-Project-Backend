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
        "mentee": result.data
    }

@router.get("/")
async def get_mentee_all():
    result = MenteeRepo.getAll()
    return {
        "success": True,
        "mentee": result
    }

@router.get("/{discord_id}")
async def get_mentee_id(discord_id: str):
    result = MenteeRepo.getDataByID(discord_id)
    return{
        "success": True,
        "Mentee": result
    }

@router.put("/{discord_id}")
async def update_mentee_more(discord_id: str, data:dict):
    result = MenteeRepo.updateData(discord_id, data)
    return{
        "success": True,
        "Mentee": result.data
    }

@router.put("/{discord_id}")
async def update_mentee_one_field(discord_id: str, data, field:str):
    result = MenteeRepo.updateDataField(discord_id, data, field)
    return{
        "success": True,
        "Mentee": result.data
    }

@router.delete("/{discord_id}")
async def delete_mentee_id(discord_id: str):
    result = MenteeRepo.deleteData(discord_id)
    return{
        "success": True,
        "Mentee": result.data
    }

@router.get("/")
async def getTotal():
    return MenteeRepo.getCount()
