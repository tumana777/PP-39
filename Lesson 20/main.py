# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# new_list = [str(num) for num in lst]
#
# text = ', '.join(new_list)
#
# # print(text)
#
# with open("numbers.txt", "w") as file:
#     file.writelines(text)

# with open("numbers.txt", "r") as file:
#     data = file.read()
#
# lst = data.split(", ")
#
# deserialized_list = [int(num) for num in lst]
#
# print(deserialized_list)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Student({self.name}, {self.age})"
#
# s1 = Student("Otar", 35)
#
# def student_serializer(student: Student):
#     if isinstance(student, Student):
#         return {
#             "name": student.name,
#             "age": student.age
#         }
#     return "Not a student object"
#
# serialized_student = student_serializer(s1)

# print(student_serializer(s1))

# def student_deserializer(data: dict):
#     if isinstance(data, dict):
#         return Student(data["name"], data["age"])
#     return "Not a dictionary"
#
# print(student_deserializer(serialized_student))

import json

# student = {
#     "name": "Otar",
#     "age": 35,
#     "grades": [10, 20, 30],
#     "address": {
#         "city": "Tbilisi",
#         "street": "Kambarov street",
#     },
#     "is_active": True,
#     "float": 3.14,
#     "tuple": (1, 2, 3),
#     "none": None
# }

# serialized_student = json.dumps(student, indent=4)

# print(serialized_student)

# deserialized_student = json.loads(serialized_student)
#
# print(deserialized_student)

# from datetime import datetime
#
# student1 = {
#     "name": "Otar",
#     "age": 35,
#     "grades": [10, 20, 30],
#     "address": {
#         "city": "Tbilisi",
#         "street": "Kambarov street",
#     },
#     "is_active": True,
#     "float": 3.14,
#     "tuple": (1, 2, 3),
#     "none": None
# }
#
# student2 = {
#     "name": "Saba",
#     "age": 25,
#     "grades": [10, 20, 30],
#     "address": {
#         "city": "Tbilisi",
#         "street": "Kambarov street",
#     },
#     "is_active": False,
#     "float": 3.14,
#     "tuple": (1, 2, 3),
#     "none": None
# }
#
# students = [student1, student2]
#
# students_data = {
#     "count": len(students),
#     "created_at": str(datetime.now()),
#     "students": students,
# }

# with open("student.json", "w") as file:
#     json.dump(students_data, file, indent=4)

# with open("student.json", "r") as file:
#     data = json.load(file)
#
# print(data)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Student({self.name}, {self.age})"
#
# s1 = Student("Otar", 35)
#
# def student_serializer(student: Student):
#     if isinstance(student, Student):
#         return {
#             "name": student.name,
#             "age": student.age
#         }
#     return "Not a student object"

# print(student_serializer(s1))
#
# print(student_deserializer(serialized_student))

# with open("student1.json", "w") as file:
#     json.dump(s1, file, default=student_serializer, indent=4)

# def student_deserializer(data: dict):
#     if isinstance(data, dict):
#         return Student(data["name"], data["age"])
#     return "Not a dictionary"
#
# with open("student1.json", "r") as file:
#     student = json.load(file, object_hook=student_deserializer)
#
# print(student)

import pickle

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Student({self.name}, {self.age})"

# s1 = Student("Otar", 35)

# serialized_student = pickle.dumps(s1)
#
# deserialized_student = pickle.loads(serialized_student)
#
# print(deserialized_student)

# with open("student2.pkl", "wb") as file:
#     pickle.dump(s1, file)

# with open("student2.pkl", "rb") as file:
#     student = pickle.load(file)
#
# print(student)

# with open("student3.pkl", "wb") as file:
#     pickle.dump(student1, file)


# with open("student3.pkl", "rb") as file:
#     data = pickle.load(file)
#
# print(data)


