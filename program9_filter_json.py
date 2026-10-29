import json

json_data = """
[
    {"name": "Sanjivani", "marks": 85},
    {"name": "Priya", "marks": 95},
    {"name": "Neha", "marks": 68}
]
"""

students = json.loads(json_data)

passed_students = [
    student for student in students
    if student["marks"] >= 70
]

print(json.dumps(passed_students, indent=3))
