from database import supabase

class MentorRepo():

    @staticmethod
    def getAll():
        response = (
            supabase
            .table("Mentors")
            .select("*")
            .execute()
        )
        return response.data

    @staticmethod
    def createData(data: dict):
        return (
            supabase
            .table("Mentors")
            .insert(data)
            .execute()
        )


    @staticmethod
    def getDataByID(id: int):
        return (
            supabase
            .table("Mentors")
            .select("*")
            .eq("id", id)
            .execute()
        ).data

    @staticmethod
    def updateData(id: int, data: dict):
        return (
            supabase
            .table("Mentors")
            .update(data)
            .eq("id", id)
            .execute()
        )

    @staticmethod
    def updateDataField(id: int, data, field: str):
        return (
            supabase
            .table("Mentors")
            .update({field: data})
            .eq("id", id)
            .execute()
        )

    @staticmethod
    def deleteData(id: int):
        return (
            supabase
            .table("mentors")
            .delete()
            .eq("id", id)
            .execute()
        )

    @staticmethod
    def getCount():
        return len(
            (
                supabase
                .table("Mentors")
                .select("*")
                .execute()
            ).data
        )