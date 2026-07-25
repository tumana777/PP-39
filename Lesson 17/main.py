# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C:
#     def show(self):
#         print("C")
#
# class D(A, C):
#     pass
#
# print(D.__mro__)

# d = D()
# d.show()

# b = B()
# b.show()

# c = C()
# c.show()

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def start(self):
#         print(f"Starting {self.make} {self.model}")
#
#     def accelerate(self, mph):
#         self.speed += mph
#         print(f"Accelerating to {self.speed} mph")
#
#     def slow_down(self, mph):
#         self.speed -= mph
#         print(f"Slowing down to {self.speed} mph")
#
#     def brake(self):
#         self.speed = 0
#         print("Braking")
#
# class ElectricVehicle:
#     def __init__(self, battery_capacity):
#         self.battery_capacity = battery_capacity
#         self.battery_level = 100
#
#     def charge(self, percent):
#         self.battery_level += percent
#         print(f"Battery level: {self.battery_level}%")
#
#     def discharge(self, percent):
#         self.battery_level -= percent
#         print(f"Battery level: {self.battery_level}%")
#
# class ElectricSUV(Vehicle, ElectricVehicle):
#     def __init__(self, make, model, year, battery_capacity):
#         Vehicle.__init__(self, make, model, year)
#         ElectricVehicle.__init__(self, battery_capacity)
#
#     def info(self):
#         print(f"This is an {self.make} {self.model} with a battery capacity of {self.battery_capacity} KW.")
#
# tesla = ElectricSUV("Tesla", "Model X", 2020, 100)
#
# tesla.info()
# tesla.discharge(20)
# tesla.accelerate(10)
# tesla.accelerate(20)


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __add__(self, other):
#         return self.age + other.age
#
#     def __str__(self):
#         return f"Student name: {self.name} and age: {self.age}"

    # def __repr__(self):
    #     return f"Student({self.name}, {self.age})"

# s1 = Student("Otar", 35)
# s2 = Student("Ana", 25)

# print(s1)
# print(s2)

# print(s1 + s2)


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#
#         return f"{other} is not a Vector instance"
#
#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x - other.x, self.y - other.y)
#         return f"{other} is not a Vector instance"
#
#     def __mul__(self, other):
#         if isinstance(other, (int, float)):
#             return Vector(self.x * other, self.y * other)
#         return f"{other} is not a number"
#
#     def __truediv__(self, other):
#         if isinstance(other, (int, float)):
#             return Vector(self.x / other, self.y / other)
#         return f"{other} is not a number"
#
#     def __eq__(self, other):
#         return isinstance(other, Vector) and self.x == other.x and self.y == other.y
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
# v1 = Vector(7, 2)
# v2 = Vector(3, 4)
#
# print(v1 + v2)


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __call__(self):
#         return f"I am callable instance"
#
# s1 = Student("Otar", 35)
#
#
# print(s1())


# class Multiplier:
#     def __init__(self, x):
#         self.x = x
#
#     def __call__(self, y):
#         return self.x * y
#
# a = Multiplier(8)
#
# print(a(9))

# class Test:
#     def __new__(cls, a):
#         if a < 5:
#             return None
#
#         print("I am a new method")
#         return super().__new__(cls)
#
#     def __init__(self, a):
#         print("I am an init method")
#
# t = Test(4)

# class MyMeta(type):
#     def __new__(mcls, name, bases, attrs):
#         print(f"name: {name}")
#         print(f"bases: {bases}")
#         attrs["created_by"] = "Admin"
#         print(f"attrs: {attrs}")
#         return super().__new__(mcls, name, bases, attrs)
#
# class A:
#     pass
#
# class Test(A, metaclass=MyMeta):
#     x = 7
#
#     def test(self):
#         print("test")
#
# t = Test()
#
# print(t.created_by)
















