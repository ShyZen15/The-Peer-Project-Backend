from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from App.schemas.availability import Availability
from App.schemas.trackMentor import TrackMentor
from App.schemas.hear import Hear

class Assignment(BaseModel):
    mentorID: str
    menteeID: str
    confidenceScore: float = Field(ge=0.0, le=1.0)
    reason: str
    assigned: bool = False