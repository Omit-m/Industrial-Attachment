dc = {"name": "nahid", "age": 20}

# print(dc.get("email", "nahid-euit.com"))

p = dc.setdefault("email", "nahid-euit.com")
# print(p)
# print(dc)


p = dc.setdefault("name", "****")
print(p)
print(dc)
