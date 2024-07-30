# Question 1 :
posation = str( input(" Enter thr  member posation : "))
exprience = int( input(" Enter thr  member exprience : "))

if posation== "manager" and exprience >=5:
    print(" Eligible for special benefit")
elif posation == "teamlead" and  exprience>=1 and exprience <=5 :
    print(" Eligible for special benefit")
elif posation == "staff" and   exprience > 7:
    print(" Eligible for special benefit")
else:
    print(" not Eligible for special benefit")





