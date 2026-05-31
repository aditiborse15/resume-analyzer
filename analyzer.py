import pdfplumber
import re

class ResumeAnalyzer:

    def extract_text(self, pdf_file):
        text = ""
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
        return text.lower()

    def extract_keywords(self, text):
        # Remove special characters, split into words
        words = re.findall(r'\b[a-zA-Z][a-zA-Z0-9+#.]*\b', text)
        # Filter out common stop words
        stop_words = {
            "the", "and", "for", "with", "this", "that", "have",
            "from", "are", "was", "were", "will", "been", "has",
            "your", "our", "their", "they", "which", "about",
            "into", "than", "also", "can", "all", "any", "but",
            "not", "you", "we", "in", "of", "to", "a", "an",
            "is", "it", "at", "on", "or", "as", "be", "by",
            "if", "so", "do", "my", "me", "he", "she", "his",
            "her", "its", "who", "how", "what", "when", "where"
        }
        return set(w.lower() for w in words if w.lower() not in stop_words and len(w) > 2)

    def analyze(self, resume_text, job_description):
        resume_keywords = self.extract_keywords(resume_text)
        jd_keywords = self.extract_keywords(job_description)

        # Find matched and missing keywords
        matched = resume_keywords.intersection(jd_keywords)
        missing = jd_keywords.difference(resume_keywords)

        # Calculate match score
        if len(jd_keywords) == 0:
            score = 0
        else:
            score = round((len(matched) / len(jd_keywords)) * 100, 2)

        return {
            "score": score,
            "matched_keywords": sorted(matched),
            "missing_keywords": sorted(missing),
            "total_jd_keywords": len(jd_keywords),
            "total_matched": len(matched)
        }