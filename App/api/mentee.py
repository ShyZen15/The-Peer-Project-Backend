from fastapi import APIRouter, HTTPException
from postgrest.exceptions import APIError
from App.schemas.mentees import MenteesRegistration
from App.repository.MenteeRepo import MenteeRepo

router = APIRouter(
    prefix="/mentee",
    tags=["Mentee"]
)

@router.post("/")
async def register_mentee(
    mentees: MenteesRegistration
): 
    try:
        result = MenteeRepo.createData(
            mentees.model_dump(mode="json")
        )

        return {
            "success": True,
            "mentee": result.data
        }
    except APIError as e:
        if "discord_id" in str(e):
            raise HTTPException(
                status_code=409,
                detail="Discord ID already exists"
            )
        
        raise HTTPException(
            status_code=500,
            detail="Database error."
        )

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

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Mentee Not Found"
        )
    return{
        "success": True,
        "mentor": result
    }

@router.put("/{discord_id}")
async def update_mentee_more(discord_id: str, data:dict):

    existing = MenteeRepo.getDataByID(discord_id)

    if not existing:
        raise HTTPException(
            status_code=404,
            detail="Mentor not Found."
        )

    try:
        result = MenteeRepo.updateData(discord_id, data)
        return{
            "success": True,
            "Mentee": result.data
        }
    except APIError as e:
        if "discord_id" in str(e):
            raise HTTPException(
                status_code=409, 
                detail="Discord ID already exists"
            )
        raise HTTPException(
            status_code=500,
            detail="Database error."
        )

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
