# 🧠 Job Description Skill Extractor

An intelligent AI-based recruitment assistant built using LangChain, FastAPI, and Streamlit that automatically extracts skills, experience, and education from Job Descriptions and matches them against uploaded resumes using Large Language Models.

---

# 🌐 Project Overview

Recruiters often spend significant time manually reviewing resumes and matching them with job descriptions. This process is repetitive, time-consuming, and prone to human error.

This project automates the recruitment screening workflow using AI and LLMs by:

* Extracting structured information from Job Descriptions
* Parsing uploaded resumes
* Matching resume skills with required job skills
* Generating match scores and missing skill analysis

The system helps recruiters make faster and smarter hiring decisions.

---

# 🌐 Live Demo

🔗 [Job Description Skill Extractor](https://huggingface.co/spaces/swapnapapireddy3/job-description-skill-extractor)
# 📝 Job Description Skill Extractor

# 🎯 Objectives

* Automate Job Description skill extraction
* Parse and analyze resumes intelligently
* Match candidate skills with JD requirements
* Generate ATS-style match scores
* Identify missing skills
* Reduce manual recruitment effort

---

# ✨ Features

* 📄 Resume Upload (PDF/DOCX/TXT)
* 🧠 AI-Based Job Description Analysis
* 🔍 Skill Extraction using LLMs
* 📊 Resume vs JD Matching
* 📈 Match Score Generation
* ❌ Missing Skill Identification
* ⚡ FastAPI Backend APIs
* 🌐 Streamlit Interactive Frontend
* 🔐 Environment Variable Security
* 🤖 Gemini LLM Integration

---

# 🏗️ System Workflow

```text id="jlwm2e"
User Uploads Resume
        │
        ▼
Streamlit Frontend
        │
        ▼
FastAPI Backend
        │
        ├── Resume Parsing
        │
        ├── JD Skill Extraction using LLM
        │
        ├── Skill Matching Logic
        │
        ▼
AI Analysis Result
        │
        ▼
Frontend Output Display
```

---

# ⚙️ How It Works

## 1️⃣ Resume Upload

The user uploads a resume in:

* PDF
* DOCX
* TXT format

---

## 2️⃣ Job Description Input

The recruiter enters the Job Description into the application.

---

## 3️⃣ Resume Parsing

The system extracts text from uploaded resumes using:

* PyPDF2
* python-docx

---

## 4️⃣ AI-Based JD Extraction

The Job Description is sent to the Gemini LLM using LangChain prompts.

The LLM extracts:

* Skills
* Experience
* Education

---

## 5️⃣ Skill Matching

The system compares:

* Resume skills
* JD skills

and generates:

* Match Score
* Matched Skills
* Missing Skills

---

## 6️⃣ Final Output

The final structured AI analysis is displayed on the frontend.

---

# 📊 Example Output

```json id="jlwm3e"
{
  "skills": [
    "Python",
    "SQL",
    "AWS"
  ],
  "experience": "3 years",
  "education": "B.Tech",
  "match_score": "75%",
  "matched_skills": [
    "Python",
    "SQL"
  ],
  "missing_skills": [
    "AWS"
  ]
}
```

---

# 🛠️ Tech Stack

| Component         | Technology            |
| ----------------- | --------------------- |
| Frontend          | Streamlit             |
| Backend           | FastAPI               |
| LLM Framework     | LangChain             |
| LLM               | Google Gemini         |
| Resume Parsing    | PyPDF2, python-docx   |
| Authentication    | Environment Variables |
| API Communication | Requests              |
| Data Format       | JSON                  |

---

# 📂 Project Structure

```bash
RESUME_JD_MATCHER/
│
├── app.py                    # Streamlit Frontend
├── main.py                   # FastAPI Backend
├── jd_extractor.py           # JD Extraction Logic
├── matcher.py                # Resume Matching Logic
├── resume_parser.py          # Resume Text Extraction
├── requirements.txt
├── .env
└── README.md
```

---

# 🚀 Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/resume-jd-matcher.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd resume-jd-matcher
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Generate API Key from:

[Google AI Studio](https://aistudio.google.com/app/apikey?utm_source=chatgpt.com)

---

# ▶️ Run Backend Server

```bash
uvicorn main:app --reload
```

Backend runs on:

```text id="jlwm4e"
http://127.0.0.1:8000
```

---

# ▶️ Run Frontend

Open another terminal and run:

```bash
streamlit run app.py
```

Frontend runs on:

```text id="jlwm5e"
http://localhost:8501
```

---

# 📌 Example Job Description

```text id="jlwm6e"
Looking for a Python Developer with SQL, AWS, and Docker skills with 3 years of experience.
```

---

# 📌 Example Resume Skills

```text id="jlwm7e"
Python
SQL
AWS
```

---

# 📌 Generated Analysis

```text id="jlwm8e"
Match Score: 75%

Matched Skills:
- Python
- SQL
- AWS

Missing Skills:
- Docker
```

---

# 🔮 Future Enhancements

* 📊 ATS Score Dashboard
* 📂 Multiple Resume Screening
* 🧠 Semantic Skill Matching
* 🗄️ Vector Database Integration
* 🤖 RAG Pipeline
* 📧 Email Notifications
* ☁️ Cloud Deployment
* 👥 Multi-User Authentication

---

# ⚠️ Challenges Faced

* Resume text extraction inconsistencies
* LLM JSON formatting issues
* Prompt engineering optimization
* Backend-frontend integration
* Avoiding hallucinations in AI output

---

# 📄 License

This project is developed for educational and learning purposes.

---

# 👨‍💻 Author

**Swapna Papireddy**
AI/ML Developer | Python Full Stack Developer | Generative AI Enthusiast



