from fastapi import APIRouter
from App.schemas.assignment import Assignment
from App.repository.AssignRepo import AssignRepo

router = APIRouter(
    prefix="/Assign",
    tags=["Assign"]
)

@router.post("/")
async def register_mentor(
    assigns: Assignment
): 
    result = AssignRepo.createData(
        assigns.model_dump(mode="json")
    )

    return {
        "success": True,
        "assign": result.data
    }

@router.get("/")
async def get_assign_all():
    result = AssignRepo.getAll()
    return {
        "success": True,
        "assign": result
    }

@router.get("/{id}")
async def get_assign_id(id: int):
    result = AssignRepo.getDataByID(id)
    return{
        "success": True,
        "assign": result
    }

@router.put("/{id}")
async def update_assign_more(id: int, data:dict):
    result = AssignRepo.updateData(id, data)
    return{
        "success": True,
        "assign": result.data
    }

@router.put("/{id}")
async def update_assign_one_field(id: int, data, field:str):
    result = AssignRepo.updateDataField(id, data, field)
    return{
        "success": True,
        "assign": result.data
    }

@router.delete("/{id}")
async def delete_assign_id(id: int):
    result = AssignRepo.deleteData(id)
    return{
        "success": True,
        "assign": result.data
    }

@router.get("/")
async def getTotal():
    return AssignRepo.getCount()
