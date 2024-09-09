"""
[*] Sum of First N Natural Numbers:
Write a program that takes an input n from the user and prints the sum of the first n natural numbers using a for loop.
"""
n=int(input(" Enter the number : "))
sum=0

for i in range(1,n+1):
    sum+=i
print(f" sum of the first ({n}) natural numbers = {sum} ")
# print(" sum of the first (" + str(n) + ") natural numbers = " + str(sum))