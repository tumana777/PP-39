import requests
import faker

url = "https://crudcrud.com/api/31c29820a60448a994e7d3afc1854beb/users"

fake = faker.Faker()

for _ in range(20):
    user = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "address": fake.address(),
        "age": fake.random_int(min=18, max=60)
    }
    requests.post(url, json=user)