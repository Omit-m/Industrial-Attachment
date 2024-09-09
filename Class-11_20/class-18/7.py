class Person:
    def __init__(self, name, age):
        self.real_name = name
        self.age = age
        self.name = "DEMO"
        self.degress = ["ssc", "hsc", "bsc"]


nahid = Person(name="nahid", age=28)
shajjad = Person(name="shajjad", age=20)

print("======= nahid ===========")
print(nahid.name)
print(nahid.real_name)
print(nahid.degress)


print("======= shajjad ===========")
print(shajjad.name)
print(shajjad.real_name)
print(shajjad.degress)
