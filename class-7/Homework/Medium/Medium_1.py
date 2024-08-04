"""
[*] Multiplication Table:
    Write a program that prints the multiplication table of a number entered by the user using a for loop.
"""
n = int(input(" Enter a number : "))
multiplication = 0
print(f" {n}th multiplication table :")
for i in range(1,11):
    multiplication = n * i
    print(f"  {n} * {i} = {multiplication} ")

