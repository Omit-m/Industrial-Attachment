# style - 2

# from <module> import <function1> , <variable>

from converter import fahrenheit_to_celsius, miles_to_kilometers

f_inp = int(input("Enter a fahrenheit temp : "))

celcius = fahrenheit_to_celsius(f=f_inp)

print(f"{celcius} *C ")
