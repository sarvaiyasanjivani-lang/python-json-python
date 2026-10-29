import json

invalid_json = '{"name":"Sanjivani", "age": }'

try:
    data = json.loads(invalid_json)
    print(data)
except json.JSONDecodeError as error:
    print("Invalid JSON:", error)
