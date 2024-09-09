dc = {
    "name": "nahid",
    "age": 20,
    "email": "example.com",
    "occupation": "service holder",
}


# refernce
# dc1 = dc

# unpack
dc1 = {**dc}


dc["name"] = "abc"
dc1["occupation"] = "business"

print(dc)
print(dc1)
