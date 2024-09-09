# refential data type : list , dictionary
ls = [1, 2, 3, 4]
ps = [*ls]

print(ps)
print(ls)

ls[1] = 20

print("========================")
print(ps)
print(ls)

print("========================")
ps[-1] = 500
print(ps)
print(ls)
