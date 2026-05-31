# 📄 Resume Analyzer

A Python-based web application that analyzes your resume against a job description and gives you an **ATS match score** with keyword insights — helping you improve your resume before applying.

---

## 🌐 Live Demo
👉 [Click here to view the app](https://embpnl3u8ounxjcukvfq5z.streamlit.app/) 

---

## 🎯 What is ATS?
ATS (Applicant Tracking System) is software used by companies to automatically filter resumes based on keywords. This tool simulates that process so you can optimize your resume before applying.

---

## ✨ Features

- 📤 Upload resume in PDF format
- 📋 Paste any job description
- 📊 Get an instant ATS match score (%)
- ✅ See which keywords matched
- ❌ See which keywords are missing
- 💡 Get suggestions to improve your resume
- 🟢 Color-coded feedback (Excellent / Good / Low match)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web interface |
| pdfplumber | PDF text extraction |
| OOP | Modular and scalable code structure |
| Regex | Keyword extraction and text processing |
| Git & GitHub | Version control |

---

## 📁 Project Structure

```
resume_analyzer/
│
├── app.py              # Streamlit UI - main application file
├── analyzer.py         # Python logic - OOP class for resume analysis
├── requirements.txt    # Python dependencies

```

---

## ⚙️ How It Works

```
1. User uploads Resume (PDF)
         ↓
2. pdfplumber extracts all text from PDF
         ↓
3. User pastes Job Description
         ↓
4. App extracts keywords from both texts
         ↓
5. Compares and finds matched & missing keywords
         ↓
6. Calculates ATS match score and shows results
```

---

## 🚀 How to Run Locally

### Step 1 — Clone the repository
```bash
git clone https://github.com/aditiborse15/resume-analyzer.git
cd resume-analyzer
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Run the app
```bash
streamlit run app.py
```

### Step 4 — Open in browser
```
http://localhost:8501
```

---

## 🧪 How to Use

1. Run the app
2. Upload your resume as a **PDF file**
3. Go to **LinkedIn**, **Naukri**, or **Internshala**
4. Copy a job description and paste it in the app
5. Click **Analyze Resume**
6. View your match score and missing keywords
7. Add missing keywords to your resume and retest!

---

## 📸 Screenshots

<img width="1847" height="839" alt="image" src="https://github.com/user-attachments/assets/732f0865-dce6-4a71-93d5-eabb935c454b" />

<img width="1877" height="876" alt="image" src="https://github.com/user-attachments/assets/e81708df-ec8d-43a2-aede-3d977a52f387" />


---

## 📊 Score Interpretation

| Score | Meaning |
|---|---|
| 75% and above | ✅ Excellent — well aligned with the job |
| 50% - 74% | ⚠️ Good — add some missing keywords |
| Below 50% | ❌ Low — resume needs improvement |

---

## 💡 What I Learned

- Extracting text from PDF files using pdfplumber
- Text processing and keyword extraction using Regex
- Implementing Object-Oriented Programming (OOP) in Python
- Building interactive web applications with Streamlit
- Understanding how ATS (Applicant Tracking System) works
- Version control using Git and GitHub
- Deploying Python apps on Streamlit Cloud

---

## 🔮 Future Improvements

- [ ] Add support for DOCX resume format
- [ ] Show keyword density analysis
- [ ] Add AI-powered resume suggestions
- [ ] Support multiple job description comparison
- [ ] Add login so users can save their analysis history

---

## 👩‍💻 Author

**Aditi Avinash Borse**
- 📧 aditi.borse15@gmail.com
- 🔗 [LinkedIn](https://linkedin.com/in/aditi-borse-0916b2321)
- 🐙 [GitHub](https://github.com/aditiborse15)

---

⭐ If you found this project helpful, please give it a star on GitHub!
