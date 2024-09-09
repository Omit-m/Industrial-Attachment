class Person:

    def name(self,age, S_N ):
        print(f"Name : {self }\n Age : {age},\nSchool Name : {S_N}")

    def call_all(self):
        Person.name("omit",23,"Faridpur Polytechnic Institute" )



preson = Person()
preson.call_all()