from App.schemas.mentor import MentorRegistration
from App.schemas.mentees import MenteesRegistration

class ProfileFormatter:

    @staticmethod
    def mentor_profile(mentor: MentorRegistration) -> str:
        """
        Convert a mentor profile into natural language for embedding.
        """

        return f"""
        Full Name: {mentor.full_name}

        Current Status: {mentor.currentStatus}

        College: {mentor.college}

        Tracks:
        {", ".join(mentor.track)}

        Availability:
        {mentor.Availability}

        Why Mentor:
        {mentor.why_mentor}

        Additional Information:
        {mentor.additionalInfo}
        """.strip()

    @staticmethod
    def mentee_profile(mentee: MenteesRegistration) -> str:
        """
        Convert a mentee profile into natural language for embedding.
        """

        return f"""
        Full Name: {mentee.full_name}

        Availability:
        {mentee.Availability}

        Interested Track:
        {", ".join(mentee.track)}

        Needs Help In:
        {mentee.helpIn}

        Additional Information:
        {mentee.additionalInfo}
        """.strip()