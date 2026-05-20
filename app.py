import streamlit as st
from prompt import prompt
from parser import parser
from model import get_model
import PyPDF2
import docx
from langfuse.langchain import CallbackHandler

langchain_handler = CallbackHandler()

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📄",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp {
    background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
    color:white;
}

.hero-title {
    text-align:center;
    font-size:60px;
    font-weight:800;
    background: linear-gradient(to right,#38bdf8,#818cf8);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-subtitle {
    text-align:center;
    color:#d1d5db;
    font-size:20px;
    margin-bottom:40px;
}

.section-card {
    background: rgba(255,255,255,0.05);
    padding:25px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.08);
    margin-bottom:20px;
}

.skill-pill {
    display:inline-block;
    padding:10px 18px;
    margin:6px;
    border-radius:30px;
    background: linear-gradient(to right,#2563eb,#7c3aed);
    color:white;
    font-size:14px;
    font-weight:600;
}

.stButton > button {
    width:100%;
    height:60px;
    border-radius:18px;
    border:none;
    background: linear-gradient(to right,#2563eb,#7c3aed);
    color:white;
    font-size:20px;
    font-weight:700;
}

textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 18px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    '<div class="hero-title">📄 AI Resume Matcher</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">AI Powered Resume Screening & Skill Gap Analysis</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# PDF EXTRACTOR
# ---------------------------------------------------

def extract_text_from_pdf(file):

    pdf_reader = PyPDF2.PdfReader(file)
    text = ""

    for page in pdf_reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text

# ---------------------------------------------------
# DOCX EXTRACTOR
# ---------------------------------------------------

def extract_text_from_docx(file):

    doc = docx.Document(file)
    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text

# ---------------------------------------------------
# TEXT EXTRACTOR
# ---------------------------------------------------

def extract_text(file):

    if file.name.endswith(".pdf"):
        return extract_text_from_pdf(file)

    elif file.name.endswith(".docx"):
        return extract_text_from_docx(file)

    elif file.name.endswith(".txt"):
        return str(file.read(), "utf-8")

    return ""

# ---------------------------------------------------
# MAIN SECTION
# ---------------------------------------------------

left_col, right_col = st.columns(2)

with left_col:

    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.subheader("📋 Enter Job Description")

    job_description = st.text_area(
        "",
        height=300,
        placeholder="Paste Job Description Here..."
    )

    st.markdown('</div>', unsafe_allow_html=True)

with right_col:

    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.subheader("📄 Upload Resume")

    resume_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx", "txt"]
    )

    st.write("✅ Supported Formats: PDF, DOCX, TXT")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# BUTTON
# ---------------------------------------------------

if st.button("🚀 Analyze Resume"):

    if job_description.strip() == "":
        st.warning("Please enter Job Description")

    elif resume_file is None:
        st.warning("Please upload Resume")

    else:

        try:

            # ---------------------------------------------------
            # EXTRACT RESUME TEXT
            # ---------------------------------------------------

            resume_text = extract_text(resume_file)

            # ---------------------------------------------------
            # LOAD MODEL
            # ---------------------------------------------------

            model = get_model()

            # ---------------------------------------------------
            # CREATE CHAIN
            # ---------------------------------------------------

            chain = prompt | model | parser

            # ---------------------------------------------------
            # INVOKE CHAIN
            # ---------------------------------------------------

            result = chain.invoke(
                {
                    "job_description": job_description,
                    "resume": resume_text
                },
                config={
                    'callbacks': [langchain_handler],
                    'tags': ["ai-resume-matcher"],
                    'metadata': {
                        'project': "AI Resume Matcher"
                    }
                }
            )

            st.success("✅ Resume Analysis Completed")

            # ---------------------------------------------------
            # MATCH PERCENTAGE
            # ---------------------------------------------------

            st.markdown("## 📊 Match Percentage")

            st.progress(result.match_percentage / 100)

            st.markdown(
                f"### ✅ Match Score: {result.match_percentage}%"
            )

            # ---------------------------------------------------
            # EXPERIENCE & EDUCATION
            # ---------------------------------------------------

            c1, c2 = st.columns(2)

            with c1:
                st.subheader("💼 Experience")
                st.write(result.experience)

            with c2:
                st.subheader("🎓 Education")
                st.write(result.education)

            # ---------------------------------------------------
            # REQUIRED SKILLS
            # ---------------------------------------------------

            st.markdown("## 🛠 Required Skills")

            for skill in result.required_skills:
                st.markdown(
                    f'<span class="skill-pill">{skill}</span>',
                    unsafe_allow_html=True
                )

            # ---------------------------------------------------
            # CANDIDATE SKILLS
            # ---------------------------------------------------

            st.markdown("## 👨‍💻 Candidate Skills")

            for skill in result.candidate_skills:
                st.markdown(
                    f'<span class="skill-pill">{skill}</span>',
                    unsafe_allow_html=True
                )

            # ---------------------------------------------------
            # MATCHED SKILLS
            # ---------------------------------------------------

            st.markdown("## ✅ Matched Skills")

            for skill in result.matched_skills:
                st.markdown(
                    f'<span class="skill-pill">{skill}</span>',
                    unsafe_allow_html=True
                )

            # ---------------------------------------------------
            # MISSING SKILLS
            # ---------------------------------------------------

            st.markdown("## ❌ Missing Skills")

            for skill in result.missing_skills:
                st.markdown(
                    f'<span class="skill-pill">{skill}</span>',
                    unsafe_allow_html=True
                )

            # ---------------------------------------------------
            # REJECTION REASONS
            # ---------------------------------------------------

            st.markdown("## 🚫 Possible Rejection Reasons")

            st.write(result.rejection_reason)

            # ---------------------------------------------------
            # RECOMMENDATIONS
            # ---------------------------------------------------

            st.markdown("## 📚 Recommended Skills to Learn")

            for skill in result.recommendations:
                st.markdown(
                    f'<span class="skill-pill">{skill}</span>',
                    unsafe_allow_html=True
                )

            # ---------------------------------------------------
            # JSON OUTPUT
            # ---------------------------------------------------

            st.markdown("## 📦 JSON Output")

            st.json(result.model_dump())

        except Exception as e:

            st.error(f"Error: {str(e)}")