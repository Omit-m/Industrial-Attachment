list =[56,78,34,5,67,90,32]

sum=1

result = [sum := sum* i for i in list]  # its call Walrus (syntext =variable := expression)
print(sum)  # output = 143284377600
print(result)  # output =[56, 4368, 148512, 742560, 49751520, 4477636800, 143284377600]