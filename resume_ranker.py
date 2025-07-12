# resume_ranker.py — Core Logic for AI Resume Ranking

import os
from groq import Groq
import fitz  # PyMuPDF
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def summarize_resume_gpt(text):
    prompt = f"""
    You are an summarizer agent that s expert in summarizing resumes.
    You are an AI assistant helping a busy recruiter quickly screen resumes.

    Given the resume text below, write a concise 2-line summary that highlights:

    - Key skills or technologies
    - Relevant job titles or experience
    - Industry/domain focus
    - Achievements or responsibilities (if notable)

    Avoid generic phrases. Focus on what's *relevant to hiring*.
    Resume:
    {text}

    Summary:
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def process_resumes(job_description, resume_paths):
    jd_embedding = embedder.encode(job_description, convert_to_tensor=True)
    results = []

    for path in resume_paths:
        text = extract_text_from_pdf(path)
        embedding = embedder.encode(text, convert_to_tensor=True)
        score = util.pytorch_cos_sim(jd_embedding, embedding).item()
        summary = summarize_resume_gpt(text)
        results.append({
            "Candidate": os.path.basename(path),
            "Fit Score": round(score, 3),
            "Summary": summary
        })

    results.sort(key=lambda x: x['Fit Score'], reverse=True)
    return pd.DataFrame(results)
