import requests

URL = "https://jsonplaceholder.typicode.com/posts"

#   Syntax : requests.method_name(params)
response = requests.get(URL, timeout=5)

print(response.status_code)

data = response.json()

# print(data)

for each_post in data:
    print(each_post)
    print("--------------------------")