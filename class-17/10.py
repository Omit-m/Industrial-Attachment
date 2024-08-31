# all()


condition1 = True
condition2 = True
condition3 = True
condition4 = True
condition5 = True

# if condition1 and condition2 and condition3 and condition4 and condition5:
#     print("----")

conditions = [condition1, condition2, condition3, condition4, condition5]


print(all(conditions))

if all(conditions):
    print("-----")
