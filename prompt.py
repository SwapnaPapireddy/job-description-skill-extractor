from langchain_core.prompts import PromptTemplate
from parser import parser

# ---------------------------------------------------
# PROMPT TEMPLATE
# ---------------------------------------------------

prompt = PromptTemplate(

    template="""
You are an AI Resume Screening and Skill Gap Analysis System.

Your task is to analyze the given Job Description and Candidate Resume.

You must carefully compare both inputs and provide structured output.

---------------------------------------------------
TASKS TO PERFORM
---------------------------------------------------

1. Extract required skills from Job Description

2. Extract candidate skills from Resume

3. Identify matched skills

4. Identify missing skills

5. Extract required experience

6. Extract required education

7. Calculate resume match percentage

8. Provide possible rejection reasons

9. Recommend skills candidate should improve

---------------------------------------------------
JOB DESCRIPTION
---------------------------------------------------

{job_description}

---------------------------------------------------
CANDIDATE RESUME
---------------------------------------------------

{resume}

---------------------------------------------------
IMPORTANT INSTRUCTIONS
---------------------------------------------------

- Match skills intelligently
- Avoid duplicate skills
- Give realistic rejection reasons
- Recommendations should focus on missing skills
- Match percentage should be between 0 to 100
- Output must be in structured JSON format

---------------------------------------------------
FORMAT INSTRUCTIONS
---------------------------------------------------

{format_instructions}

""",

    # ---------------------------------------------------
    # INPUT VARIABLES
    # ---------------------------------------------------

    input_variables=[
        "job_description",
        "resume"
    ],

    # ---------------------------------------------------
    # FORMAT INSTRUCTIONS FROM PARSER
    # ---------------------------------------------------

    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)