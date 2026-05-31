import streamlit as st
from analyzer import ResumeAnalyzer

st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 Resume Analyzer")
st.markdown("Upload your resume and paste a job description to see how well you match!")

analyzer = ResumeAnalyzer()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📤 Upload Resume (PDF)")
    uploaded_file = st.file_uploader("Choose your resume", type=["pdf"])

with col2:
    st.subheader("📋 Paste Job Description")
    job_description = st.text_area("Paste the job description here", height=250)

if st.button("🔍 Analyze Resume", use_container_width=True):
    if uploaded_file is None:
        st.error("❌ Please upload your resume PDF!")
    elif job_description.strip() == "":
        st.error("❌ Please paste the job description!")
    else:
        with st.spinner("Analyzing your resume..."):
            resume_text = analyzer.extract_text(uploaded_file)
            results = analyzer.analyze(resume_text, job_description)

        st.markdown("---")
        st.subheader("📊 Results")

        # Score display
        score = results["score"]
        col1, col2, col3 = st.columns(3)
        col1.metric("Match Score", f"{score}%")
        col2.metric("Keywords Matched", results["total_matched"])
        col3.metric("Total JD Keywords", results["total_jd_keywords"])

        # Score color feedback
        if score >= 75:
            st.success(f"✅ Excellent match! Your resume is well aligned with this job.")
        elif score >= 50:
            st.warning(f"⚠️ Good match! Consider adding some missing keywords.")
        else:
            st.error(f"❌ Low match. Your resume needs improvement for this role.")

        # Progress bar
        st.progress(int(score))

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matched Keywords")
            if results["matched_keywords"]:
                for kw in results["matched_keywords"]:
                    st.markdown(f"- `{kw}`")
            else:
                st.write("No keywords matched.")

        with col2:
            st.subheader("❌ Missing Keywords")
            if results["missing_keywords"]:
                for kw in results["missing_keywords"]:
                    st.markdown(f"- `{kw}`")
            else:
                st.write("No missing keywords — perfect match!")

        st.markdown("---")
        st.caption("💡 Tip: Add the missing keywords to your resume to improve your ATS score!")