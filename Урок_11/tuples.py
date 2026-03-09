# Представьте, что вы разрабатываете программу для учёта товаров в магазине.
# Каждый товар представлен набором характеристик: название товара, цена и количество единиц на складе.
# Эти характеристики удобно хранить в виде кортежа.
#
# Напишите программу, которая позволяет вводить новые товары,
# выводить полный список всех товаров,
# находить самый дорогой товар и подсчитывать общую стоимость всех товаров на складе.
from statistics import quantiles

inventory = []

def add_item(name, price, quantity):
    item = (name, float(price), int(quantity))
    inventory.append(item)

def show_inventory():
    if not inventory:
        print("Склад пустой")
    else:
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item[0]} | Цена: {item[1]:2f} руб. | Количество: {item[2]} шт.")

def find_most_expensive():
    if not inventory:
        return None
    most_expensive = max(inventory, key=lambda x: x[1])
    return f"Самый дорогой товар: {most_expensive[0]}, цена: {most_expensive[1]:.2f} руб."

def total_value():
    if not inventory:
        return 0
    total = sum([price * quantity for _, price, quantity in inventory])
    return round(total, 2)

while True:
    print("\nМеню:")
    print("1. Добавить товар")
    print("2. Показать весь склад")
    print("3. Найти самый дорогой товар")
    print("4. Посчитать общую стоимость товаров")
    print("5. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        name = input("Название товара: ")
        price = input("Цена: ")
        quantity = input("Количество: ")
        add_item(name, price, quantity)
    elif choice == '2':
        show_inventory()
    elif choice == '3':
        result = find_most_expensive()
        if result is not None:
            print(result)
    elif choice == '4':
        value = total_value()
        print(f"Общая стоимость товаров на складе: {value:.2f} рублей.")
    elif choice == '5':
        break
    else:
        print("Некорректный выбор пункта меню")

# my_tuple3 = (10, 20, 30)
# my_tuple4 = (10, 20, 40)
#
# print( my_tuple3 < my_tuple4 )
# for item in my_tuple:
#     print(item)

# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

# my_tuple1 = (2,3,4,5,6,2,3,4,2)
# my_tuple2 = (5,6,7,8)
# combined_tuple = my_tuple1 + my_tuple2
# print(combined_tuple)
# repeated_tuple = my_tuple2*3
# print(repeated_tuple)
#
# print( 2 in my_tuple1 )
# print( 9 in my_tuple1 )
#
# print( my_tuple1.count(3) )
# print( my_tuple1.index(4) )
# my_tuple = (1,2,3,4)
#
# my_tuple[0] = 10
#
# print(my_tuple[0])
# print(my_tuple[2])
#
# print(my_tuple[-1])
#
# print(my_tuple)
#
# single_tuple = (5, )
# print(single_tuple)