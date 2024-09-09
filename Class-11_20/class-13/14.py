
import random

# Sample data for generating random names
first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack", "John", "Emma", "Liam", "Olivia", "Noah", "Sophia", "James", "Mia", "Lucas", "Charlotte"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson"]

# Function to generate a random person
def generate_random_person():
    return \
    {
        "name": f"{random.choice(first_names)} {random.choice(last_names)}",
        "salary": random.randint(40000, 100000),
        "is_active": random.choice([True, False]),
        "age": random.randint(25, 50)
    }
# Generate a list of 300 people
people = [generate_random_person() for _ in range(300)]

#   Generate a list of 300 people
# people=[]
# for i in range(300):
#     peoples=generate_random_person()
#     people.append(peoples)

# Example: Output the list
for person in people:
    print(f" {person},")