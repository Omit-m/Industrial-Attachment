helping_variable = 1

condition = helping_variable <= 10 # true

while condition:
    print(f"* {condition}")

    helping_variable = helping_variable + 1
    
    condition = helping_variable <= 10

