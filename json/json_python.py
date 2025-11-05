import json

json_example = '''{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": ["Python", "QA Automation", "API Testing"],
  "address": {
    "city": "Москва",
    "zip": "101000"
  }
}'''


data = json.loads(json_example)

with open("json_example.json", "r", encoding="utf-8") as file:
    data_r = json.load(file)
    print(data_r)

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)


