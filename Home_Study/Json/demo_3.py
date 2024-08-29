import json

x = ('{ '
    '"name":"John",'
    '"age":30,'
    '"city":"New York"}'
    )

y = json.loads(x)

print(y["age"])
# the result is a Python dictionary
print(y)