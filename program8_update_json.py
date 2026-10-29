import json
from pathlib import Path

file_path = Path("student.json")

student = {
    "name": "Sanjivani",
    "marks": 90
}

file_path.write_text(
    json.dumps(student, indent=2),
    encoding="utf-8"
)

data = json.loads(file_path.read_text(encoding="utf-8"))
data["marks"] = 90
data["grade"] = "A"

file_path.write_text(
json.dumps(data, indent=3),
    encoding="utf-8"
)

print("Updated data:", data)
