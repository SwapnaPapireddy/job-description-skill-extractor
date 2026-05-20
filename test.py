from prompt import prompt
from parser import parser
from model import get_model

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

model = get_model()

# ---------------------------------------------------
# CREATE CHAIN
# ---------------------------------------------------

chain = prompt | model | parser

# ---------------------------------------------------
# SAMPLE JOB DESCRIPTION
# ---------------------------------------------------

job_description = """
We are looking for a Python Developer with experience in
Machine Learning, SQL, Pandas, NumPy, Deep Learning,
and Streamlit.

Candidate should have knowledge of AWS, Docker,
and REST APIs.

Minimum 2 years of experience required.

Bachelor's Degree in Computer Science or related field.
"""

# ---------------------------------------------------
# SAMPLE RESUME
# ---------------------------------------------------

resume = """
John Doe

Skills:
Python, SQL, Pandas, NumPy, Streamlit, Machine Learning

Experience:
1 year Python Developer Intern

Education:
Bachelor of Technology in Computer Science
"""

# ---------------------------------------------------
# INVOKE CHAIN
# ---------------------------------------------------

result = chain.invoke({
    "job_description": job_description,
    "resume": resume
})

# ---------------------------------------------------
# PRINT OUTPUT
# ---------------------------------------------------

print("\n========== AI RESUME MATCHER OUTPUT ==========\n")

print("Required Skills:")
print(result.required_skills)

print("\nCandidate Skills:")
print(result.candidate_skills)

print("\nMatched Skills:")
print(result.matched_skills)

print("\nMissing Skills:")
print(result.missing_skills)

print("\nExperience:")
print(result.experience)

print("\nEducation:")
print(result.education)

print("\nMatch Percentage:")
print(result.match_percentage)

print("\nRejection Reason:")
print(result.rejection_reason)

print("\nRecommendations:")
print(result.recommendations)

print("\nJSON OUTPUT:")
print(result.model_dump())