a = "apple"
b = "banana"
c = "apple"
d = "APPle"
e = "bananaa"


r = a == b  # False
r = a == c  # True
r = a == d  # False
r = b == e  # False
r = b != e  # True

# Case sensitive
print(r)
