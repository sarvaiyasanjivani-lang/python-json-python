import json

with open("employee.json", "r", encoding="utf-8") as file:
    employee = json.load(file)

print("Employee:", employee["name"])
print("Department:", employee["department"])
print("Salary:", employee["salary"])
