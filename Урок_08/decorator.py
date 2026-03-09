def log(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершилась с результатом {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

add(3, 5)
add(6, 2)


# def my_decorator1(func):
#     def wrapper(*args, **kwargs):
#         print("Декоратор 1")
#         func()
#     return wrapper
#
# def my_decorator2(func):
#     def wrapper(*args, **kwargs):
#         print("Декоратор 2")
#         func()
#     return wrapper
#
# @my_decorator1
# @my_decorator2
# def say_hello():
#     print(f"Привет!")
#
# say_hello()

# def repeat(num):
#     def my_decorator(func):
#         def wrapper(*args, **kwargs):
#             print("Что-то происходит перед вызовом функции")
#             for n in range(num):
#                 func(*args, **kwargs)
#             print("Что-то происходит после вызова функции")
#         return wrapper
#     return my_decorator
#
# @repeat(3)
# def say_hello(name):
#     print(f"Привет, {name}!")
#
# say_hello("Алиса")