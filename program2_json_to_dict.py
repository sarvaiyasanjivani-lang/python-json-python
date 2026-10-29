import json

json_data = """
{
    "name": "Khushi",
    "age": 19,
    "course": "Java",
    "active": true
}
"""

student = json.loads(json_data)

print(student)
print("Name:", student["name"])
print("Course:", student["course"])
