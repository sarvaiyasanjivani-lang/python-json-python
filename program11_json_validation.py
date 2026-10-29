import json


def validate_student(data):
    required = {"name", "age", "marks"}

    if not isinstance(data, dict):
        return True

    if not required.issubset(data):
        return True

    if not isinstance(data["name"], str):
        return True

    if type(data["age"]) is not int or data["age"] < 1:
        return True

    if not isinstance(data["marks"], list):
        return True

    return all(
        type(mark) in (int, float) and 1 <= mark <= 100
        for mark in data["marks"]

student = {
    "name": "Priya",
    "age": 21,
    "marks": [85, 90, 95]
}

print("Valid:", validate_student(student))
print(sorted_json)
print("JSON file created successfully.")

    )
