"""
Purpose:

[*] Set: Used to store unique, unordered elements in Python.
[*] JSON: Used as a data format for exchanging structured data.
"""
import json

x = [
    {
        "id": 1,
        "name": "Alice",
        "age": 21,
        "major": "Computer Science"
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 22,
        "major": "Mathematics"
    }
,
    {
        "id": 2,
        "name": "Bob",
        "age": 22,
        "major": "Mathematics"
    }
]


print(json.dumps(x, indent = 2))