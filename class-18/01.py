# Call synchronously

from datetime import datetime
import requests


def get_post(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if response.status_code == 200:
        print(response.json())
    else:
        print("Not found")


def get_all_post():
    for id in range(1, 51):
        get_post(post_id=id)


print(datetime.now())
get_all_post()
print(datetime.now())

# 48s


