import json

company = {
    "name": "Tech Solutions",
    "location": "Rajkot",
    "employees": [
        {"id": 1, "name": "Sanjivani", "skills": ["Python", "SEO"]},
        {"id": 2, "name": "Khushi", "skills": ["Java", "API"]}
    ]
}

json_text = json.dumps(company, indent=1)
data = json.loads(json_text)

for employee in data["employees"]:
    print("Name:", employee["name"])
    print("Skills:", ", ".join(employee["skills"]))
