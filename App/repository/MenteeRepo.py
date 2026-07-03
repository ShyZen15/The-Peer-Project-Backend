from database import supabase

class MenteeRepo():

    @staticmethod
    def getAll():
        response = (
            supabase
            .table("Mentees")
            .select("*")
            .execute()
        )
        return response.data

    @staticmethod
    def createData(data: dict):
        return (
            supabase
            .table("Mentees")
            .insert(data)
            .execute()
        )


    @staticmethod
    def getDataByID(id: int):
        return (
            supabase
            .table("Mentees")
            .select("*")
            .eq("id", id)
            .execute()
        ).data

    @staticmethod
    def updateData(id: int, data: dict):
        return (
            supabase
            .table("Mentees")
            .update(data)
            .eq("id", id)
            .execute()
        )

    @staticmethod
    def updateDataField(id: int, data, field: str):
        return (
            supabase
            .table("Mentees")
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
            .table("Mentees")
            .delete()
            .eq("id", id)
            .execute()
        )

    @staticmethod
    def getCount():
        return len(
            (
                supabase
                .table("Mentees")
                .select("*")
                .execute()
            ).data
        )