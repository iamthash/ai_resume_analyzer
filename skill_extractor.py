import pandas as pd
import re
from pathlib import Path
DATA_FILE = Path(__file__).parent / "data" / "skill_dictionary.csv"
def load_skills():
    df = pd.read_csv(DATA_FILE)
    return df["skill"].dropna().str.lower().tolist()
SKILL_DICTIONARY = load_skills()
def extract_skills(text):
    text = text.lower()
    found_skills = []
    for skill in SKILL_DICTIONARY:
        pattern = r"(?<![a-z0-9])" + re.escape(skill) + r"(?![a-z0-9])"
        if re.search(pattern, text):
            found_skills.append(skill)
    return found_skills