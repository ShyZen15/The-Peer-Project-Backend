from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import List, Optional
from availability import Availability
from track import Track
from hear import Hear

class MentorRegistration(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    display_name: str
    email: EmailStr
    discord_id: str
    reddit_id: Optional[str] = None
    track: List[Track]
    helpIn: str
    Availability: Availability
    hear: List[Hear]
    additionalInfo: str