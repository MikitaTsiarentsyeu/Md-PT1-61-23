import json

test_json = '{"width":500,"height":500,"resolution":96,"quality":96,"settings":[{"filename":"_preview1.jpg","seek":10},{"filename":"_preview2.jpg","seek":35},{"filename":"_preview3.jpg","seek":70},{"filename":"_preview4.jpg","seek":95}]}'

obj = json.loads(test_json)
print(type(obj))
print(obj['settings'])

obj['settings'] = tuple(obj['settings'])

with open("test.json", 'w') as f:
    json.dump(obj, f)

with open("test.json", 'r') as f:
    new_obj = json.load(f)

print(obj)
print(new_obj)