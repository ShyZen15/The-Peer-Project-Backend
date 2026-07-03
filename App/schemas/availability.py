from enum import Enum

class Availability(str, Enum):
    ONE_TWO = "1-2 sessions/month"
    THREE_FOUR = "3-4 sessions/month"
    FLEX = "Flexible"