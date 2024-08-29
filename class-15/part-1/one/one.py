# DRY (Don't repeat yourself -> reusablity)
# import syntax

# style - 1
# import <module>

import converter


print(f">>> is : {__name__}")

f_inp = int(input("Enter a fahrenheit temp : "))

celcius = converter.fahrenheit_to_celsius(f=f_inp)


print(f"{celcius} *C ")
print(converter.PI)
