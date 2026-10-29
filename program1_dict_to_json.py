import json

student = {
    "name": "Sanjivani",
    "age": 22,
    "marks": [98, 81, 74],
    "passed": True
}

json_data = json.dumps(student, indent=3)

print(json_data)
