# all()


condition1 = True
condition2 = False
condition3 = True
condition4 = False
condition5 = True

# if condition1 or condition2 or condition3 or condition4 or condition5:
#     print("----")

conditions = [condition1, condition2, condition3, condition4, condition5]


print(any(conditions))

if all(conditions):
    print("-----")
