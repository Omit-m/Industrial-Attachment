class Person:

    def __init__(self):
        """Constructor"""
        print("hello")
        """
        print("hello", self)
        
        output : 
            create reference by self : 
            hello <__main__.Person object at 0x0000017D7317C1D0>
            hello <__main__.Person object at 0x0000017D7317C250>
            hello <__main__.Person object at 0x0000017D7317C290>
            hello <__main__.Person object at 0x0000017D7317C2D0>
            """


# object creation
obj1 = Person()
obj2 = Person()
obj3 = Person()
obj4 = Person()
