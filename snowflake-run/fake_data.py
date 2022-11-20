from faker import Faker

fake = Faker()
Faker.seed(11)
for i in range(10):
    with open('data.txt', 'a') as file:
        file.write("('{}', '{}'),\n".format(fake.street_address(), fake.first_name()))
    