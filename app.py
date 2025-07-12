# app.py — Streamlit Frontend for AI Resume Ranker

import streamlit as st
import pandas as pd
import os
import tempfile
from resume_ranker import process_resumes  # Core logic file

st.set_page_config(page_title="AI Resume Ranker", layout="centered")
st.title("📊 AI Resume Summary & Ranking Tool")
st.markdown("Upload a job description and multiple resumes. Let AI do the filtering.")

# Upload Job Description
jd_text = st.text_area("📄 Paste Job Description", height=200)

# Upload resumes
uploaded_files = st.file_uploader("📎 Upload Resumes (PDF only, multiple)", type=["pdf","png","docx","jpeg"], accept_multiple_files=True)

if st.button("🚀 Run AI Resume Ranker"):
    if not jd_text:
        st.error("Please provide a Job Description.")
    elif not uploaded_files:
        st.error("Please upload at least one resume.")
    else:
        with st.spinner("Processing resumes with AI..."):
            # Save uploaded files to temp directory
            with tempfile.TemporaryDirectory() as resume_dir:
                resume_paths = []
                for uploaded_file in uploaded_files:
                    file_path = os.path.join(resume_dir, uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.read())
                    resume_paths.append(file_path)

                # Process resumes
                ranked_df = process_resumes(jd_text, resume_paths)

                st.success("✅ Done! Here's your ranked list:")
                st.dataframe(ranked_df)
                st.download_button("⬇ Download CSV", data=ranked_df.to_csv(index=False),
                                   file_name="ranked_candidates.csv", mime="text/csv")
