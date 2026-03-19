class Dog:
    breed = "Дворняга"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Создан объект класса Dog")

    def bark(self):
        return f"{self.name}: гав гав!"

    @staticmethod
    def info():
        print("Это класс Dog")

    def __del__(self):
        print(f"Объект с именем ${self.name} удалён!")