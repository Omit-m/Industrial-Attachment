li = [1,2,3,4]

new_li = []

for x in li:
    new_li.append(2 * x)

print(new_li)

# use list compraction 

new_li = [2 *  x for x in li] 
print(new_li)