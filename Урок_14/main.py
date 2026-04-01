from animal import Animal

class Cat(Animal):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age, breed)
        print("Создан кот")

    def speak(self):
        print(f"{self.nickname}: мяу мау")

    def run(self):
        print(f"{self.nickname} побежал(а)")


class Bird(Animal):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age, breed)
        print("Создана птица")

    def fly(self):
        print(f"{self.nickname} полетел(а)")

class FlyingCat(Cat, Bird):
    pass

cat = Cat("Барсик", 4, "Дворняга")

print(cat.nickname)
cat.run()
cat.speak()

flyingCat = FlyingCat("Летающий Барсик", 7, "-")
flyingCat.run()
flyingCat.fly()