import json


json_string = input()
json_object = json.loads(json_string)
print(type(json_object))
print(json_object)
