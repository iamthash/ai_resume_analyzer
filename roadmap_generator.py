def generate_roadmap(missing_skills):
    roadmap = []
    for skill in missing_skills:
        roadmap.append({
            "skill": skill,
            "action": f"Learn the basics of {skill}",
            "practice": f"Complete a small project using {skill}",
        })
    return roadmap