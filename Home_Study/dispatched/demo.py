from functools import singledispatch


@singledispatch
def identy(value):
    pass
    @identy.register(int)
    def _(value):
        print( f"Handling integer : {value **2}")
    @identy.register(str)
    def _(value):
        print(f"Handling string : {value}")
    @identy.register(float)
    def _ (value):
        print(f"Handling floats : {value}")
    @identy.register(bool)
    def _ (value):
        print(f"Handling bools : {value}")
identy(12)
identy("omit")
identy('O')
identy(True)
identy(3.1416)
identy("omit")