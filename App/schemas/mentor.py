from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import List, Optional
from availability import Availability
from trackMentor import TrackMentor
from hear import Hear

class MentorRegistration(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    currentStatus: str
    college: str
    email: EmailStr
    track: List[TrackMentor]
    proof: HttpUrl
    reddit_id: Optional[str] = None
    discord_id: str
    display_name: str
    Availability: Availability
    why_mentor : str
    hear: List[Hear]
    additionalInfo: str
