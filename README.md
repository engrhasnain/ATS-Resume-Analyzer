# 🧠 AI Resume Analyzer (ATS Optimizer)

AI Resume Analyzer is an intelligent web application built using **LangChain**, **Groq API**, and **Streamlit** that analyzes resumes against Applicant Tracking System (ATS) criteria. It identifies weaknesses, provides specific skill-level suggestions, applies corrections, and generates a downloadable optimized resume with an ATS compatibility score.

---

## 🚀 Features

- 📂 **Upload Resume** (PDF or DOCX)  
- 🤖 **ATS Analysis powered by Groq LLM**  
- 🎯 **Specific Suggestions** (e.g., *"Add Python and FastAPI to Skills"*)  
- 📊 **ATS Score** (0–100) based on resume strength  
- 📥 **Corrected Resume Download** (DOCX format)  
- 📝 **Job Description Matching** (optional) to tailor recommendations   
---
## 🏗️ Tech Stack

| Technology     | Purpose                                      |
|----------------|----------------------------------------------|
| **LangChain**  | Orchestrates AI interactions and prompt chaining. |
| **Groq API**   | Provides fast, cost-efficient LLM inference. |
| **Streamlit**  | Interactive web interface.                  |
| **pdfplumber** | Extracts text from PDF resumes.             |
| **python-docx**| Edits and generates Word documents.         |
| **fpdf**       | Enables optional PDF export.                |

## Project Structure
```bash
ats_resume_analyzer/
│
├── app.py                     # Main Streamlit app
├── groq_llm.py                # Groq LLM initialization
├── resume_parser.py           # Extract text from PDF/DOCX
├── resume_analyzer.py         # Analyze resume and generate suggestions
├── resume_editor.py           # Apply AI suggestions and create updated resume
├── requirements.txt           # Dependencies
└── utils/
    ├── __init__.py
    └── file_handler.py        # Utility for saving uploaded files
```

## ⚙️ Installation
### 1. Clone the Repository
``` bash
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
```
### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Set Groq API Key
Create a .env file in the root directory:
```bash
GROQ_API_KEY=your_groq_api_key_here
Or directly edit groq_llm.py and replace "YOUR_GROQ_API_KEY".
```

### ▶️ Running the App
Start the Streamlit app:
```bash
streamlit run app.py
```

## 🔥 Future Improvements
- ✏️ Highlight changes directly in the resume file.  
- 📌 Add keyword-matching score for job descriptions.  
- 📄 Export to PDF with tracked changes.  
- 🌐 Multi-language support.  
- 🔗 Integration with LinkedIn profile import.  

---

## 🤝 Contributing
Contributions are welcome!  

1. Fork the repository  
2. Create a feature branch  
3. Submit a pull request  

---

## 🛡 License
This project is licensed under the **MIT License**.

