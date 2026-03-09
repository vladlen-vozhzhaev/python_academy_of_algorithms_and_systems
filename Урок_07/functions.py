def square1(x):
    return x**2

square = lambda x: x**2
print(square(5))
print(square1(5))

# x = 10
#
# def change_x():
#     global x
#     x = 20
#     y = 40
#
# change_x()
# print(x)
#print(y)


# def g():
#     print("Hello!")
#     return
#     print("bye!")
#
# g()
# def multiply(a, b):
#     return a*b
#
# result = multiply(5,5)
# print(result)

# def printUserInfo(**kwargs):
#     message = f"Информация о пользователе:\n"
#     for key, value in kwargs.items():
#         message += f"- {key.capitalize()}: {value}\n"
#     print(message)
#
# printUserInfo(name="Иван", age=20, city="Москва")


# def sum_numbers(*args):
#     total = sum(args)
#     print(total)
#
# sum_numbers(1,2,3,4,5)


# def f(a,b=100):
#     print(a+b)
#
# f(20)
# #f(b=5)
# f(6,1)
# f(8,3)

# def sayHello(name):
#     print(f"Hello {name}")
#
# sayHello("Oleg")
# sayHello("Ivan")
# sayHello("Olga")

# def sayHelloWorld():
#     print("Hello world!")
#
# sayHelloWorld()
# sayHelloWorld()
# sayHelloWorld()