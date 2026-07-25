# empty_dict = {}
# empty_dict = dict()
#
# print(empty_dict)
# print(type(empty_dict))

# names = ["John", "Jane", "Bob", "Alice"]
# ages = [25, 30, 40, 52]
# cities = ["New York", "London", "Paris", "Tokyo"]
#
# # John is 25 years old
#
# for i in range(len(names)):
#     print(f"{names[i]} is {ages[i]} years old")

# names = {
#     "John": 25,
#     "Jane": 30,
#     "Bob": 40,
#     "Alice": 52
# }

# my_dict = {
#     "str": "This is a string",
#     1: "This is an integer",
#     3.14: "This is a float",
#     True: "This is a boolean",
#     None: "This is a None",
#     (1, 2, 3): "This is a tuple"
# }
#
# print(my_dict)


# names = {
#     "John": 25,
#     "Jane": 30,
#     "Bob": 40,
#     "Alice": 52,
#     "John": 65
# }
#
# print(names)


# my_dict = {
#     "str": "This is a string",
#     2: "This is an integer",
#     3.14: "This is a float",
#     True: "This is a boolean",
#     None: "This is a None",
#     (1, 2, 3): "This is a tuple",
#     "list": [1, 2, 3, 4, 5],
#     "dict": {"key": "value"}
# }
#
# print(my_dict)

# names = {
#     "John": 25,
#     "Jane": 30,
#     "Bob": 40,
#     "Alice": 52,
#     "john": 65,
#     "Ana": 29,
#     "Davit": 45
# }

# print(names["John"])
# print(names["Alice"])
# print(names["john"])

# names["Otar"] = 35
# names["Ana"] = 35

# print(names)

# names = {
#     "John": 25,
#     "Jane": 30,
#     "Bob": 40,
#     "Alice": 52,
#     "john": 65,
#     "Ana": 29,
#     "Davit": 45,
# }

# print(len(names))

# for key in names:
#     print(names[key])


# for key in names:
#     print(f"{key} is {names[key]} years old.")

# names = {
#     "John": 25,
#     "Jane": 30,
#     "Bob": 40,
#     "Alice": 52,
#     "john": 65,
#     "Ana": 29,
#     "Davit": 45,
# }

# print(list(names.keys()))
# print(list(names.values()))
# print(list(names.items()))

# print(names.get("Otar"))
# print(names.get("Otar", "Not found"))

# for key, value in names.items():
#     print(f"{key} is {value} years old.")

# names = {
#     "John": 25,
#     "Jane": 30,
#     "Bob": 40,
#     "Alice": 52,
#     "john": 65,
#     "Ana": 29,
#     "Davit": 45,
# }

# names.update({"Otar": 35, "ana": 35})
# popped = names.pop("Bob")
# popped = names.popitem()
#
# print(names)
# print(popped)

# names = ["Otar", "Tumanishvili", "Davit", "Ana"]
#
# print(dict.fromkeys(names, 5))

# names = {
#     "John": 25,
#     "Jane": 30,
#     "Bob": 40,
#     "Alice": 52,
#     "john": 65,
#     "Ana": 29,
#     "Davit": 45,
# }

# names.setdefault("Ana", 35)
#
# print(names)

# my_dict = {i:"Hello" for i in range(10) if i % 2 == 0}
#
# print(my_dict)

products = {
    "Electonics": {
        "Laptops": {"title": "HP", "price": 1000},
        "Desktops": {"title": "Dell", "price": 2000},
        "Monitors": {"title": "Sony", "price": 3000}
    },
    "Clothing": {
        "Shirts": {"title": "Nike", "price": 500},
        "Pants": {"title": "Adidas", "price": 700},
        "Jackets": {"title": "Puma", "price": 800}
    }
}

print(products["Electonics"]["Desktops"]["price"])

# print(len(products))


