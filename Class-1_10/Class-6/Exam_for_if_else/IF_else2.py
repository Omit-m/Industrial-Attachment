# Question 2 :

midterm_exam = input("Enter the achievement grade in midterm_exam: ")
final_exam = input("Enter the achievement grade in final_exam: ")
ex_ac = input("Enter the extracurricular activity: ")

if midterm_exam == 'A' and final_exam == 'A' and ex_ac == "High":
    grad = 'A+'
elif midterm_exam in ('A', 'B') and final_exam in ('A', 'B') and ex_ac == "Moderate":
    grad = 'B'
elif midterm_exam in ('C', 'D') and final_exam in ('C', 'D') and ex_ac == "Moderate":
    grad = 'C'
elif midterm_exam == 'D' and final_exam == 'D' and ex_ac == "None":
    grad = 'D'
else:
    grad = 'No valid grade'


if grad in ('A', 'B') and ex_ac in ("Moderate", "High"):
    print("They have completed their graduation")
else:
    print("The student does not meet the above criteria")
