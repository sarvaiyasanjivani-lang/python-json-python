import json

json_one = '{"name": "Sanjivani", "age": 22}'
json_two = '{"course": "Python", "passed": true}'

data_one = json.loads(json_one)
data_two = json.loads(json_two)

merged_data = {**data_one, **data_two}

print(json.dumps(merged_data, indent=4))




