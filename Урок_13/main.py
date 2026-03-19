from dog import Dog

dog1 = Dog("Бобик", 4)
dog2 = Dog("Лайка", 3)
dog3 = Dog("Шарик", 5)

print(dog1.name)

print(dog3.bark())
print(dog2.bark())

Dog.info()

dog1.info()

del dog1

print(dog1.name)