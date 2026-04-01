class Animal:
    def __init__(self, nickname, age, breed):
        self.nickname = nickname
        self.age = age
        self.breed = breed


    def speak(self):
        print(f"{self.nickname} издаёт звук")


class Transport:
    """Базовый класс для всех видов транспорта"""

    def __init__(self, speed, capacity):
        self.speed = speed  # Скорость (км/ч)
        self.capacity = capacity  # Вместимость (человек)
        self.is_moving = False  # Двигается ли сейчас? (по умолчанию нет)

    def start(self):
        """Начать движение"""
        self.is_moving = True
        print(f"{self.__class__.__name__}: Поехали! Скорость {self.speed} км/ч")

    def stop(self):
        """Остановиться"""
        self.is_moving = False
        print(f"{self.__class__.__name__}: Остановились")

    def info(self):
        """Вывести информацию о транспорте"""
        status = "движется" if self.is_moving else "стоит"
        return f"Транспорт: скорость {self.speed} км/ч, вместимость {self.capacity} чел, сейчас {status}"