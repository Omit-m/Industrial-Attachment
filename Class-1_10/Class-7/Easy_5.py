"""
 [*] Calculate the below series:
  (1)  1 + 3 + 5 + .... + N = ? [N given by user]
    2 * 4 * 6 * .... * N = ? [N given by user]
"""
# (1)
n=int(input(" Enter the number : "))
sum=0
for i in range(1,n+1,2):
    sum+=i
print(f"sum of odd  numbers from 1 to {n} = {sum}")


# (2)

n = int(input(" Enter the number : "))
Product = 1
for i in range(2,n+1,2):
    Product = Product * i
print(f"Product of even numbers from 2 to {n} = {Product}")

