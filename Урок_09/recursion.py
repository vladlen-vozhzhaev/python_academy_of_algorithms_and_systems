# Представим, что у нас есть автомат для продажи кофе.
# Клиент даёт автомату купюру, автомат готовит кофе и выдаёт сдачу.
# Сдача выдаётся монетами: 1, 2, 5 или 10 рублей.
# Реализуем функцию которая выдаёт сдачу пользователя исходя из остатка денег после продажи кофе.
# Принимаем кол-во монет бесконечным.
#
# Задача: реализовать функцию, которая принимает в качестве параметра сумму,
# которую необходимо отдать пользователю в виде чисел (монет) 1, 2, 5, 10.

# def getChange(sum):
#     coin = 0
#     if sum>=10:
#         coin = 10
#     elif sum>=5:
#         coin = 5
#     elif sum>=2:
#         coin = 2
#     elif sum >=1:
#         coin = 1
#
#     if coin > 0:
#         print(coin)
#         getChange(sum - coin)
#
# getChange(38)

# import os
#
#
# def read_directory_contents(path):
#     # Получаем список всех файлов и директорий внутри текущего каталога
#     items = os.listdir(path)
#
#     for item in items:
#         full_path = os.path.join(path, item)  # Путь к текущему элементу
#
#         if os.path.isdir(full_path):  # Если это директория, вызываем функцию рекурсивно
#             print(f"Каталог: {full_path}")
#             read_directory_contents(full_path)  # Рекурсивный вызов
#         else:
#             print(f"Файл: {full_path}")  # Если это файл, просто выводим его путь
#
#
# # Вызов функции для чтения списка файлов из папки /path
# read_directory_contents("C:\java")

# 5! = 5×4×3×2×1=120

# def factorial(n):
#     if n == 0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# print(factorial(5))

def f():
    f()

f()