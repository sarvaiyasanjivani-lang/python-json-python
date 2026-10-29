import json

employee = {
    "id": 102,
    "name": "Rajvi",
    "department": "IT",
    "salary": 8000
}

with open("employee.json", "w", encoding="utf-8") as file:
    json.dump(employee, file, indent=2)
