from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser

# ---------------------------------------------------
# PYDANTIC OUTPUT STRUCTURE
# ---------------------------------------------------

class ResumeMatcher(BaseModel):

    # REQUIRED SKILLS FROM JOB DESCRIPTION
    required_skills: List[str] = Field(
        description="Skills required from job description"
    )

    # CANDIDATE SKILLS FROM RESUME
    candidate_skills: List[str] = Field(
        description="Skills extracted from candidate resume"
    )

    # MATCHED SKILLS
    matched_skills: List[str] = Field(
        description="Skills matched between job description and resume"
    )

    # MISSING SKILLS
    missing_skills: List[str] = Field(
        description="Skills missing in candidate resume"
    )

    # EXPERIENCE
    experience: str = Field(
        description="Required years of experience"
    )

    # EDUCATION
    education: str = Field(
        description="Required education qualification"
    )

    # MATCH PERCENTAGE
    match_percentage: float = Field(
        description="Percentage of resume matching with job description"
    )

    # REJECTION REASON
    rejection_reason: str = Field(
        description="Possible reasons for candidate rejection"
    )

    # RECOMMENDATIONS
    recommendations: List[str] = Field(
        description="Skills candidate should improve"
    )

# ---------------------------------------------------
# PYDANTIC PARSER
# ---------------------------------------------------

parser = PydanticOutputParser(
    pydantic_object=ResumeMatcher
)