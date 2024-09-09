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



#if you went 1 to n, all the programs are executed with together

multiplication = 0
for j in range(1,21):
    print ( f" {j} th multiplication table :" )
    for i in range ( 1 , 11 ) :
        multiplication = j * i
        print ( f"  {j} * {i} = {multiplication} " )