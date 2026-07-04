from database import supabase

class AssignRepo():

    @staticmethod
    def getAll():
        response = (
            supabase
            .table("Assignment")
            .select("*")
            .execute()
        )
        return response.data
    
    @staticmethod
    def createData(data: dict):
        return (
            supabase
            .table("Assignment")
            .insert(data)
            .execute()
        )
    
    @staticmethod
    def getDataByID(id: int):
        return (
            supabase
            .table("Assignment")
            .select("*")
            .eq("id", id)
            .execute()
        ).data
    
    @staticmethod
    def updateData(id: int, data: dict):
        return (
            supabase
            .table("Assignment")
            .update(data)
            .eq("id", id)
            .execute()
        )
    
    @staticmethod
    def updateDataField(id: int, data, field: str):
        return (
            supabase
            .table("Assignment")
            .update(
                {field: data}
            )
            .eq("id", id)
            .execute()
        )

    @staticmethod
    def deleteData(id: int):
        return (
            supabase
            .table("Assignment")
            .delete()
            .eq("id", id)
            .execute()
        )

    @staticmethod
    def getCount():
        return len(
            (
                supabase
                .table("Assignment")
                .select("*")
                .execute()
            ).data
        )
