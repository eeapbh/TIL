from faker import Faker
fake = Faker('ko_KR')
fake.seed_instance(4321)
print(fake.name())
fake2 = Faker('ko_KR')
print(fake2.name())

Faker.seed(4321)
fake3 = Faker('ko_ KR')
print(fake3.name())
