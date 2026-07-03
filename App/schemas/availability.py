from enum import Enum

class Availability(str, Enum):
    ONE_TWO = "1-2 sessions/month"
    THREE_FOUR = "304 sessions/month"
    FLEX = "Flexible"