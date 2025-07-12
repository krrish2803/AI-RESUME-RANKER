# 📊 AI Resume Ranker

An AI-powered tool that **ranks candidate resumes**, generates **2-line summaries**, and scores **job-description (JD) fit** using embeddings + GPT-4 — built for founders, recruiters, and HR teams overwhelmed by resumes.

---

## 🧠 What It Does

✅ Upload multiple PDF resumes  
✅ Paste a job description  
✅ AI summarizes each resume  
✅ Fit score is calculated using cosine similarity  
✅ Candidates are ranked and exported as a table

---

## 🖼️ Example Output

| Candidate    | Fit Score | Summary                                                  |
|--------------|-----------|----------------------------------------------------------|
| alice.pdf    | 0.92      | 5 yrs Flask backend dev. Built APIs for a fintech app.  |
| bob.pdf      | 0.81      | Python + ML engineer with NLP experience at a startup.  |
| charlie.pdf  | 0.60      | Junior dev with internship in QA, skilled in Selenium.  |

---

## 🚀 How It Works

1. 🧾 **Resume Parsing**: Extracts text from PDF using `PyMuPDF`  
2. 📐 **Embedding + Scoring**: Uses `MiniLM` to encode resumes + JD, compares with cosine similarity  
3. ✍️ **Summary Generation**: GPT-4 summarizes resume into 2 recruiter-friendly lines  
4. 📊 **Ranking**: Sorted table with candidate, score, and summary  
5. 📥 **Export**: Download CSV of ranked candidates

---

## ⚙️ Tech Stack

### 🧾 Parsing & Embedding
- `PyMuPDF` for PDF resume text extraction
- `SentenceTransformers` (`all-MiniLM-L6-v2`) for embeddings
- `Cosine Similarity` (pytorch) for JD fit scoring

### ✍️ Summarization
- `OpenAI GPT-4` via Chat API
- Prompt-based 2-line summaries

### 💻 UI
- `Streamlit` frontend for upload, scoring, and table display

### 📦 Optional Add-ons
- `n8n` for automation: email resume → rank → send back
- `ChromaDB` or `FAISS` for scalable resume storage

---

## 🧪 Installation

```bash
git clone https://github.com/your-username/ai-resume-ranker.git
cd ai-resume-ranker
pip install -r requirements.txt
```
