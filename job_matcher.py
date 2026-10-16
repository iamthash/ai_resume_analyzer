import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skill_extractor import extract_skills
DATA_FILE = Path(__file__).parent / "data" / "job_roles.csv"
def load_job_roles():
    df = pd.read_csv(DATA_FILE)
    return {
        row["role"]: [
            skill.strip().lower()
            for skill in row["required_skills"].split(",")
        ]
        for _, row in df.iterrows()
    }
JOB_ROLES = load_job_roles()
def calculate_match(resume_text, required_skills):
    if not required_skills:
        return 0.0
    resume_skills = extract_skills(resume_text)
    if not resume_skills:
        return 0.0
    common_skills = set(resume_skills) & set(required_skills)
    if not common_skills:
        return 0.0
    resume_text_for_matching = " ".join(resume_skills)
    required_text = " ".join(required_skills)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([
        resume_text_for_matching,
        required_text,
    ])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)
def recommend_roles(resume_text):
    recommendations = []
    for role, required_skills in JOB_ROLES.items():
        score = calculate_match(resume_text, required_skills)
        recommendations.append({
            "role": role,
            "match_score": score,
        })
    recommendations.sort(
        key=lambda item: item["match_score"],
        reverse=True,
    )
    return recommendations[:3]