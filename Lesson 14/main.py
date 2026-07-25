# file = open('test.txt', 'r')
#
# data = file.read()
#
# file.close()

# data1 = file.read()

# print(data1)

# file = open('inner/inner.txt', 'r')
#
# data = file.read()
#
# file.close()
#
# print(data)

# try:
#     file = open('../inner.txt', 'r')
#     data = file.read()
#     file.close()
# except FileNotFoundError:
#     data = "File not found"
#
# print(data)

# file = open('test.txt', 'rt')
#
# data = file.read()
#
# file.close()
#
# # print(data)
# print(type(data))

# file = open('test.txt', 'rt')
#
# print(file.readable())
# print(file.writable())
#
# file.close()

# file = open('test.txt', 'rt')
#
# data = file.read(18)
#
# file.close()
#
# print(data)


# file = open('test.txt', 'rt')
#
# data = file.read()
#
# file.seek(0)
#
# data1 = file.read()
#
# file.close()
#
# print(data)
# print("==" * 10)
# print(data1)


# file = open('test.txt', 'rt')
#
# line1 = file.readline().strip("\n")
# line2 = file.readline().strip("\n")
# line3 = file.readline().strip("\n")
# line4 = file.readline().strip("\n")
#
# file.close()
#
# print(line1)
# print(line2)
# print(line3)
# print(line4)


# file = open('test.txt', 'rt')
#
# lines = file.readlines()
#
# file.close()
#
# new_lines = [line.strip("\n") for line in lines]
#
# print(new_lines)

# file = open('test1.txt', 'w')
#
# print(file.writable())
# print(file.readable())
#
# file.close()

# file = open('test1.txt', 'w+')
#
# print(file.writable())
# print(file.readable())
#
# file.close()

# file = open('test1.txt', 'x')
#
#
# file.close()

# file = open('test1.txt', 'w')
#
# file.write("Hello World")
# file.write("\n")
# file.write("Hello Python")
#
# file.close()

# file = open('test1.txt', 'a')
#
# file.write("\n25")
#
# file.close()

# with open('test1.txt', 'a') as file:
#     file.write("\n30")
#     file.write("\n35")

# names = ["Otar", "Ana", "John", "Davit", "Nino"]
#
# with open('test1.txt', 'w') as file:
#     for name in names:
#         file.write(f"{name}\n")

# names = ["Otar", "Ana", "John", "Davit", "Nino"]
#
# new_names = [f"{name}\n" for name in names]
#
# with open('test1.txt', 'w') as file:
#     file.writelines(new_names)

# name = "Otar"
#
# binary_name = name.encode("utf-8")
#
# print(binary_name)
#
# with open('name.bin', 'wb') as file:
#     file.write(binary_name)

# with open('name.bin', 'rb') as file:
#     data = file.read()
#
# name = data.decode("utf-8")
#
# print(name)


import csv

# with open('companies.csv', 'r') as file:
#     reader = csv.reader(file)
#
#     for row in reader:
#         print(row)

# with open('companies.csv', 'r') as file:
#     dict_reader = csv.DictReader(file)
#
#     for row in dict_reader:
#         print(row)


# person = {
#     "name": "Otar",
#     "age": 25,
#     "city": "Istanbul",
#     "country": "Turkey"
# }
#
# headers = ["name", "age", "city", "country"]
#
# with open('person.csv', 'w') as file:
#     writer = csv.DictWriter(file, fieldnames=headers)
#     writer.writeheader()
#     writer.writerow(person)

from faker import Faker

fake = Faker()

person = [{"first_name": fake.first_name(), "last_name": fake.last_name(), "company": fake.company()} for _ in range(50)]

headers = person[0].keys()

# print(headers)

with open('persons.csv', 'w') as file:
    dict_writer = csv.DictWriter(file, fieldnames=headers)
    dict_writer.writeheader()
    dict_writer.writerows(person)
