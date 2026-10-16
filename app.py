import streamlit as st
from resume_parser import extract_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import recommend_roles, JOB_ROLES
from roadmap_generator import generate_roadmap
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
)
st.title("AI Resume Analyzer and Job Recommendation System")
st.write(
    "Upload your resume to identify your skills, explore suitable job roles, "
    "and discover skills you could learn next."
)
uploaded_file = st.file_uploader(
    "Upload your resume (PDF or DOCX, maximum 10 MB)",
    type=["pdf", "docx"],
)
if uploaded_file is not None:
    st.write(f"**Uploaded file:** {uploaded_file.name}")
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error(
            "File is too large. Please upload a resume smaller than "
            "or equal to 10 MB."
        )
    else:
        try:
            resume_text = extract_text(uploaded_file)
            cleaned_text = clean_text(resume_text)
            if not cleaned_text:
                st.warning(
                    "No readable text found. Try a text-based PDF or DOCX file."
                )
            else:
                skills = extract_skills(cleaned_text)
                st.subheader("Skills Identified")
                if skills:
                    st.write(", ".join(skills))
                else:
                    st.write("No listed skills were found in this resume.")
                st.subheader("Top 3 Job Recommendations")
                recommendations = recommend_roles(cleaned_text)
                for item in recommendations:
                    st.write(
                        f"**{item['role']}** — "
                        f"{item['match_score']}% match"
                    )
                st.subheader("Job Match Score Chart")
                if recommendations:
                    chart_data = {
                        item["role"]: item["match_score"]
                        for item in recommendations
                    }
                    st.bar_chart(chart_data)
                st.subheader("Explore Missing Skills")
                selected_role = st.selectbox(
                    "Choose a job role",
                    list(JOB_ROLES.keys()),
                )
                required_skills = JOB_ROLES[selected_role]
                missing_skills = [
                    skill for skill in required_skills
                    if skill not in skills
                ]
                if missing_skills:
                    st.write(
                        "Skills to develop:",
                        ", ".join(missing_skills),
                    )
                    st.subheader("Learning Roadmap")
                    roadmap = generate_roadmap(missing_skills)
                    for item in roadmap:
                        st.markdown(f"**{item['skill']}**")
                        st.write(f"- Learn: {item['action']}")
                        st.write(f"- Practice: {item['practice']}")
                else:
                    st.success(
                        "All listed skills for this role were found."
                    )
                report = (
                    "AI RESUME ANALYSIS REPORT\n\n"
                    f"Uploaded file: {uploaded_file.name}\n\n"
                    "EXTRACTED SKILLS\n"
                    f"{', '.join(skills) if skills else 'No skills found'}\n\n"
                    "TOP JOB RECOMMENDATIONS\n"
                )
                for item in recommendations:
                    report += (
                        f"\n{item['role']}: "
                        f"{item['match_score']}% match"
                    )
                report += (
                    "\n\nSELECTED TARGET ROLE\n"
                    f"{selected_role}\n\n"
                    "MISSING SKILLS\n"
                    f"{', '.join(missing_skills) if missing_skills else 'None'}\n"
                )
                st.download_button(
                    label="Download Analysis Report",
                    data=report,
                    file_name="resume_analysis.txt",
                    mime="text/plain",
                )
                st.caption(
                    "Match scores are estimates based on listed skills, "
                    "not a measure of overall ability. Missing keywords "
                    "do not necessarily mean missing skills."
                )
                st.info(
                    "Privacy: This app does not intentionally save uploaded "
                    "resumes to permanent storage. Avoid uploading resumes "
                    "containing information you do not wish to share."
                )
        except Exception as error:
            st.error(f"Unable to process this resume: {error}")