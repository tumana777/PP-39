# def outer():
#     print("I am outer")
#     def inner():
#         return "I am inner"
#
#     return inner()
#
# print(outer())
import sys
# x = 8 # Global Variable
#
# def outer():
#     # x = 10 # Enclosing Variable
#     def inner():
#         # x = 5 # Local Variable
#         return x
#     return inner()
#
# print(outer())

# __name__ = "Gloabl Variable"

# def outer():
#     # __name__ = "Enclosing Variable"
#     def inner():
#         # __name__ = "Local Variable"
#         return __name__
#     return inner()
#
# print(outer())

# x = 8 # Global Variable
#
# def outer():
#     x = 10 # Enclosing Variable
#     def inner():
#         # global x
#         nonlocal x
#         x += 9
#         return x
#     return inner()
#
# print(outer())

# def outer():
#
#     def inner():
#         return "I am inner"
#
#     return inner
#
# i = outer()
#
# print(i())


# def get_multiplier(a):
#
#     def inner(b):
#         return a * b
#
#     return inner

# print(get_multiplier(8)(9))

# double = get_multiplier(2)
# multiplier_by_five = get_multiplier(5)

# print(double(8))
# print(double(10))
# print(double(7))
# print(double(4))

# print(multiplier_by_five(8))
# print(multiplier_by_five(10))
# print(multiplier_by_five(7))
# print(multiplier_by_five(4))




# def my_decorator(func):
#     def wrapper():
#         print("I am before the function")
#         func()
#         print("I am after the function")
#     return wrapper
#
# @my_decorator
# def add():
#     print("I am add function")


# @my_decorator
# def test():
#     print("I am test function")

# add(2, 4)
# test()


# def change_value(func):
#
#     def wrapper(x, y):
#         x += 2
#         y += 2
#         return func(x, y)
#
#     return wrapper
#
#
# @change_value
# def test(a, b):
#     print(f"a={a} b={b}")
#
#
# test(5, 8)


import time

# def test():
#     start_time = time.time()
#     print("I started working")
#     time.sleep(4)
#     print("I have finished working")
#     end_time = time.time()
#
#     print(f"Time taken: {end_time - start_time:.2f} seconds")

# test()

# def time_counter(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Time taken: {end_time - start_time:.2f} seconds")
#         return result
#
#     return wrapper

# @time_counter
# def test():
#     print("function execution started")
#     time.sleep(2)
#     print("function execution finished")
#
# test()

# @time_counter
# def another_test(n):
#     print("function execution started")
#     time.sleep(n)
#     print("function execution finished")
#
# another_test(3)

# def repeat(times=2):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @repeat(4)
# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Ana")

# from functools import wraps
#
# def deco(func):
#     @wraps(func)
#     def wrapper():
#         func()
#     return wrapper
#
# @deco
# def greet():
#     """Say hello"""
#     pass
#
# print(greet.__name__)
# print(greet.__doc__)


# def number_generator():
#     return [1, 2, 3]
#
# numbers = number_generator()
#
# print(numbers)

# def number_generator1():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
# numbers = number_generator1()
#
# iterator = iter(numbers)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for number in numbers:
#     print(number)

# def number_generator(n):
#     for i in range(1, n):
#         yield f"Number: {i}"
#
# numbers = number_generator(100_000)
#
# for number in numbers:
#     print(number)

# import sys
#
# def number_generator():
#     return list(range(1, 100_000_000))
#
# def number_generator1():
#     for i in range(1, 100_000_000):
#         yield i
#
# numbers = number_generator()
# numbers1 = number_generator1()
#
# print(sys.getsizeof(numbers))
# print(sys.getsizeof(numbers1))

lst = [i for i in range(100_000_000)]

gen = (i for i in range(100_000_000))



















