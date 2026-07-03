from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from App.schemas.availability import Availability
from App.schemas.trackMentor import TrackMentor
from App.schemas.hear import Hear

class MenteesRegistration(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    display_name: str
    email: EmailStr
    discord_id: str
    reddit_id: Optional[str] = None
    track: List[TrackMentor]
    helpIn: str
    Availability: Availability
    hear: List[Hear]
    additionalInfo: str