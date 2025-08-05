import streamlit as st
import json
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from resume_analyzer import analyze_resume
from resume_editor import update_resume_file
from utils.file_handler import save_uploaded_file

st.set_page_config(page_title="AI ATS Resume Analyzer", layout="centered")
st.title("📄 AI-Powered ATS Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Paste the job description (optional)")

if uploaded_file:
    file_path = save_uploaded_file(uploaded_file)

    if uploaded_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(file_path)
    else:
        resume_text = extract_text_from_docx(file_path)

    if st.button("Analyze Resume"):
        st.write("Analyzing resume... Please wait.")
        result = analyze_resume(resume_text, job_description)

        # Handle JSON response from the LLM
        try:
            result_json = json.loads(result)
        except:
            st.warning("The AI response was not in JSON format. Attempting to extract data...")
            result_json = {"score": 0, "issues": [], "suggestions": [], "corrected_resume": resume_text}

        ats_score = result_json.get("score", 0)
        st.metric("ATS Score", f"{ats_score}/100")

        st.subheader("Issues Found")
        if result_json.get("issues"):
            for issue in result_json["issues"]:
                st.write(f"- {issue}")
        else:
            st.write("✅ No major issues detected.")

        # st.subheader("Suggestions")
        # if result_json.get("suggestions"):
        #     for suggestion in result_json["suggestions"]:
        #         st.write(f"- {suggestion}")
        st.subheader("Specific Issues and Suggestions")

        if "issues" in result_json:
            st.write("### Issues")
            for issue in result_json["issues"]:
                st.write(f"- **Section**: {issue['section']} → {issue['problem']}")

        if "suggestions" in result_json:
            st.write("### Suggestions")
            for suggestion in result_json["suggestions"]:
                st.write(f"- **{suggestion['section']}**: {suggestion['action']}")

