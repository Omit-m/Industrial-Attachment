"""
[*] Find Prime Numbers:
    Write a program that prints all prime numbers between 1 and 100 using nested for loops.
"""

for num in range(1, 101):
    if num > 1 :
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
