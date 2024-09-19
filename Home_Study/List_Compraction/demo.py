list = [3, 4, 5, 6, 7, 8, 9]
sum = 0

l_C = [sum := sum + i for i in list]    # its call Walrus (syntext =variable := expression)

print(sum)  # output = 42
print(l_C)  # output = [3, 7, 12, 18, 25, 33, 42]

