# import my_module as mm
#
# print(mm.add(2, 7))
# print(mm.sub(2, 7))

from my_module import add, sub

# print(add(2, 7))
# print(sub(2, 7))

# import my_module
#
# print(my_module.add(2, 4))
#
# from app.app import test
#
# test()

import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

data = response.json()

for post in data:
    print(type(post))























