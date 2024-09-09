dc = {
    "name": "nahid",
    "age": 20,
    "email": "example.com",
    "occupation": "service holder",
}

p = dc.pop("occupation")
# print(p)
# print(dc)


# p = dc.pop("company")
# print(p)
# print(dc)


# print("company" in dc)
KEY_NAME = "age"

if KEY_NAME in dc:
    dc.pop(KEY_NAME)


print("final line")
print(dc)
