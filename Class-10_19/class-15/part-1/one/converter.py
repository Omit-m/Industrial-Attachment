def fahrenheit_to_celsius(f):
    celcius = (f - 32) * 5 / 9
    return round(celcius, 2)


def miles_to_kilometers(m):
    return m * 1.60934


def pounds_to_kilograms(p):
    return p * 0.453592


def inches_to_centimeters(i):
    return i * 2.54


def liters_to_gallons(l):
    return l * 0.264172


PI = 3.1416

print(f"name is : {__name__}")

if __name__ == "__main__":
    r = float(input("Enter radius : "))
    print("Area of a circle : ", 2 * PI * r)
