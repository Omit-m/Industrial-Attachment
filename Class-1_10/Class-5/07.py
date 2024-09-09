"""
APP FEATURE : User is from USA or India
"""

user_country = input("Where are you from ? ")

condition1 = user_country == "USA" or user_country == "usa"
condition2 = user_country == "India"

decision = condition1 or condition2

print(decision)
