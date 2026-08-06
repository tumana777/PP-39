# import re
#
# text = "I am learning Python"
#
# result = re.search("Python", text)
#
# if result:
#     print("ვიპოვეთ!")
# else:
#     print("ვერ ვიპოვეთ!")
import time

# import re
#
# text = "Python is great. I love Python."
#
# result = re.search("Python", text)
#
# print(result.group())

# import re
#
# text = "My age is 25"
#
# pattern = r"\w+"
#
# result = re.search(pattern, text)
#
# print(result.group())

# import re
#
# text = "Hello Python"
#
# result = re.search(r"\s", text)
#
# print(result)

# import re
#
# phone = "599123456"
#
# pattern = r"\d{9}"
#
# result = re.fullmatch(pattern, phone)
#
# if result:
#     print("სწორი ფორმატია")
# else:
#     print("არასწორი ფორმატია")

# import re
#
# phone = "59912456d"
#
# pattern = r"\d{9}"
#
# result = re.match(pattern, phone)
#
# if result:
#     print("სწორი ფორმატია")
# else:
#     print("არასწორი ფორმატია")
#
# import re
#
# text = "I have 10 apples and 25 oranges."
#
# numbers = re.findall(r"\d+", text)
#
# print(numbers)


# import re
#
# pattern = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{1,}$"
#
# emails = [
#     "oto@gmail.com",
#     "test@yahoo.com",
#     "user123@example.org",
#     "wrong-email",
#     "hello@gmail.c",
# ]
#
# for email in emails:
#     if re.fullmatch(pattern, email):
#         print(email, "→ valid")
#     else:
#         print(email, "→ invalid")