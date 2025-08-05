from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from groq_llm import get_llm

def analyze_resume(resume_text, job_description=None):
    """Analyze the resume using Groq LLM and return ATS score and very specific suggestions in JSON."""
    llm = get_llm()

    template = """
    You are an ATS (Applicant Tracking System) Resume Analyzer.
    Your job is to analyze the following resume and return ONLY a valid JSON object (no explanations, no extra text).

    Resume:
    {resume_text}

    Job Description (if provided):
    {job_description}

    The JSON must follow this structure:
    {{
        "score": <number between 0 and 100>,
        "issues": [
            {{
                "section": "<Resume section name like Skills, Experience, Education>",
                "problem": "<Clear description of the issue>"
            }}
        ],
        "suggestions": [
            {{
                "section": "<Resume section where change is needed>",
                "action": "<Specific, clear, and actionable suggestion (e.g., 'Add Python and FastAPI under Skills')>"
            }}
        ],
        "corrected_resume": "<Full corrected resume text>"
    }}

    Rules:
    - Be SPECIFIC about which skills to add or remove.
    - If experience is weak, suggest measurable improvements.
    - Do NOT add extra text outside the JSON.
    """

    prompt = PromptTemplate(template=template, input_variables=["resume_text", "job_description"])
    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run({"resume_text": resume_text, "job_description": job_description or ""})

    # Extract only the JSON part
    json_start = response.find("{")
    json_end = response.rfind("}") + 1
    if json_start != -1 and json_end != -1:
        response = response[json_start:json_end]

    return response
