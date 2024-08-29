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
]

# Filter the list to find the item with "id" = 1

y= next(item for item in x if item["id"] == 1)
# def filtered_item():
#     for item in x:
#         if item["id"] == 1:
#             return item
#
# y=filtered_item()

# Convert the filtered item to JSON with indentation
z = json.dumps(y, indent=2)

print(z)
