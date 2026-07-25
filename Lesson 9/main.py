# my_list = [5, 2, 6, 7, 4]
#
# total = 0
# count = 0
#
# for num in my_list:
#     total += num
#     count += 1
#
# print(total)
# average = total / count
# print(average)

# my_list = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
# new_list = []
#
# for item in my_list:
#     if item not in new_list:
#         new_list.append(item)
#
# print(new_list)

# from random import randint
#
# nums = [randint(-50, 50) for _ in range(20)]
# even_numbers = [num for num in nums if num % 2 == 0]
#
#
#
# print(nums)
# print(even_numbers)

# persons = [
#     ('Kelly', 'Simpson', 26),
#     ('Erika', 'Stephens', 24),
#     ('Cheryl', 'Dunn', 30),
#     ('Amy', 'Larsen', 49),
#     ('Christine', 'Gordon', 23),
#     ('Monica', 'Huff', 38),
#     ('David', 'Nixon', 36),
#     ('Cindy', 'Escobar', 41),
#     ('Cindy', 'White', 33),
#     ('Joel', 'Hall', 43),
#     ('Steven', 'Winters', 28),
#     ('Alex', 'Cole', 68),
#     ('Alex', 'Smith', 32),
#     ('Alex', 'White', 42),
#     ('Brittany', 'Thompson', 18),
#     ('Ernest', 'Young', 43),
#     ('Traci', 'Wells', 38),
#     ('Andrew', 'Flores', 61),
#     ('Christopher', 'Lewis', 29),
#     ('Kevin', 'Willis', 57),
#     ('Kayla', 'Lucas', 28),
#     ('Michelle', 'Rush', 43),
#     ('Thomas', 'Mason', 37)
# ]
#
# while True:
#     first_name = input("Enter your first name: ")
#
#     if first_name == "stop":
#         break
#
#     found_list = []
#
#     for person in persons:
#         if first_name == person[0]:
#             found_list.append(person)
#
#     if found_list:
#         last_name = input("Enter your last name: ")
#
#         if last_name == "stop":
#             break
#
#         for person in found_list:
#             if last_name == person[1]:
#                 print(f"Hello, {person[0]} {person[1]}! You are {person[2]} years old.")
#                 break
#         else:
#             print("Last name not found.")
#     else:
#         print("Name not found.")


# set1 = {2, 4, 8, 4, 7}

# print(type(set1))
# print(set1)

# set1 = {"Otar"}
# print(type(set1))

# set1 = set()
# print(type(set1))

# set1 = {2, True, "Otar", 2.5, None, (1, 2, 3)}
#
# print(set1)

# names = {"Otar", "Saba", "Davit", "Nino", "Gio", "Ana"}

# print(len(names))
# print(names)
# nums = {-100, 4, 185, 7, 9}
# print(nums)

# for name in names:
#     print(name)

# names = ["Otar", "Saba", "Davit", "Nino", "Gio", "Ana", "Otar"]
#
# names_set = set(names)
#
# name = input("Enter your name: ")
#
# if name in names_set:
#     print("Hello, ", name)
# else:
#     print("Name not found.")

# num1 = int(input("Enter a number1: "))
# num2 = int(input("Enter a number2: "))
#
# print(num1 + num2)
#
# print("Something code executed....")
#
# num1 = int(input("Enter a number1: "))
# num2 = int(input("Enter a number2: "))
#
# print(num1 + num2)
#
# print("another code executed....")
#
# num1 = int(input("Enter a number1: "))
# num2 = int(input("Enter a number2: "))
#
# print(num1 + num2)

# def add():
#     num1 = int(input("Enter a number1: "))
#     num2 = int(input("Enter a number2: "))
#
#     print(num1 + num2)
#
# add()
#
# print("Something code executed....")
#
# add()
#
# print("another code executed....")
#
# add()


# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Otar")
# greet("Gio")
# greet("Nodar")

# def greet(name, age):
#     print(f"Hello, {name}!, you are {age} years old.")
#
# greet("Otar", 35)

# def greet(first_name, last_name, age):
#     print(f"Hello, {first_name} {last_name}!, you are {age} years old.")
#
# greet(last_name="Tumanishvili", first_name="Otar", age=35)

# def greet(first_name, last_name, age):
#     print(f"Hello, {first_name} {last_name}!, you are {age} years old.")
#
# greet("Otar", last_name="Tumanishvili", age=35)

# def greet(first_name, last_name, age):
#     print(f"Hello, {first_name} {last_name}!, you are {age} years old.")
#
# # SyntaxError: positional argument follows keyword argument
# greet(age=35, last_name="Tumanishvili", "Otar")

# def add(num1, num2):
#     print("add function executed...")
#     return num1 + num2
#
# result = add(4, 8)
#
# a = result + add(5, 10)
#
# print(a)

# def add(num1, num2):
#     print("add function started...")
#     return num1 + num2
#
#
# print(add(4, 8))

# def test():
#     return "Hello", 8, 887, 98
#
#
# a, b, *c = test()
#
# print(a)
# print(b)
# print(c)























