from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.real_name = name
        self.age = age
        self.created_at = datetime.now()


nahid = Person(name="nahid", age=28)
shajjad = Person(name="shajjad", age=20)
omit = Person(name="omit", age=20)
rakibul = Person(name="rakibul", age=20)
sadi = Person(name="sadi", age=20)
kishan = Person(name="kishan", age=20)


print(nahid.created_at)
print(shajjad.created_at)
print(omit.created_at)
print(rakibul.created_at)
print(sadi.created_at)
print(kishan.created_at)
