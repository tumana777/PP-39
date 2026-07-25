# def get_factorial(n):
#     if n == 0 or n == 1:
#         return 1
#
#     return n * get_factorial(n - 1) # 5 * 4 * 3 * 2 * 1
#
# print(get_factorial(5))

# def add(a, b=6):
#     return a + b
#
# print(add(9, 3))

# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 15},
#     {"name": "Keyboard", "price": 25},
#     {"name": "Monitor", "price": 150},
#     {"name": "Power", "price": 100},
#     {"name": "Pad", "price": 10},
# ]

# def test(x):
#     return x["price"] > 100

# filtered_products = list(filter(lambda product: product["price"] % 10 == 0, products))
#
# print(filtered_products)

# import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# word = "Hello?"

# print(word.replace(".", ""))
# print(word.replace(",", ""))
# print(word.replace("?", ""))
# print(word.replace("!", ""))

# print(word.strip(string.punctuation))


# def test(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# test(name="Otar", age=35, city="Tbilisi")


# age: int = 35
# name: str = "Otar"
# active: bool = True
# height: float = 10.5

# scores: list[int] = [10, 20, 30, 40, 50]

# my_tuple: tuple[int, str, float] = (1, "Otar", 35.5)

# my_tuple = (1, "Otar", 35.5, [1, 2])
#
# print(id(my_tuple))
#
# my_tuple[3][1] = 3
#
# print(id(my_tuple))

# student: dict[str, int] = {"math": 90, "english": 80}

# my_set: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# def add(a: int, b: int):
#     return a + b
#
# print(add(1, 5))

# def test(a: str, b: str):
#     return f"{a.upper()} {b.upper()}"
#
# print(test("hello", "world"))


# def test(a: str, b: str) -> str:
#     return f"{a.upper()} {b.upper()}"
#
# print(test("hello", "world"))

# from typing import Optional
#
# email: Optional[str] = None


# email: str | None = None

# from typing import Any
#
#
# def test(a: Any):
#     print(a)


# from faker import Faker
#
# fake = Faker()
#
# print(fake.first_name())
# print(fake.last_name())
# print(fake.email())
# print(fake.address())






















