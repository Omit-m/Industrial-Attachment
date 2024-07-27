
players = ["Sakib Al Hasan", "Tamim Iqbal", "Mushfiqur Rahim", "Mahmudullah Riyad", "Liton Das"]
retired_status = [False, True, True, True, False]
ages = [37, 35, 36, 38, 29]


user_name = str(input("Enter the user_name: "))
user_is_retired = bool(input(" user_is_retired : "))
user_age = int(input("Enter the user_age: "))

if user_name in players:
    index = players.index(user_name)
    if retired_status[index] == user_is_retired or ages[index] == user_age:
        print(True)
    else:
        print(False)
else:
    print("User not found.")



