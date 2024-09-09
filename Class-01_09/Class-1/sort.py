ls=[90,49,39,26,38,27,28,19,20]
print(" Ascending")
ls1=sorted(ls)
print(ls1)
print(" Descending")
# ls2=list(sorted(ls,reverse = True)) # Approach-1 , if you want to  reverse directly a list
ls2 = ls1[::-1]     # Approach-2
print(ls2)