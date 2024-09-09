dc = {
    "name": "nahid",
    "age": 20,
    "email": "example.com",
    "occupation": "service holder",
}


def value_updater(key, value):

    if key == "email":
        value = "anything.com"

    return value


dc1 = {key: value_updater(key, value) for key, value in dc.items()}


print(dc1)
