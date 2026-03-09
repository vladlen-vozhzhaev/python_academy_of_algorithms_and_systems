import re

text1 = """
Одним прекрасным утром солнце осветило вершины гор,
птицы начали петь свои мелодичные песни,
и природа ожила новыми красками.
"""

text2 = """
Утро было таким красивым, что птицы начали свое пение,
солнце мягко касалось верхушек деревьев,
и краски природы вновь оживились.
"""

def clean_text(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    words = set(cleaned_text.split())
    return words

def calculate_similarity(set1, set2):
    intersection = len(set1 & set2) # Пересечение
    union = len(set1 | set2)
    result = (intersection/union) * 100 if union > 0 else 0
    return round(result, 2)

words_set1 = clean_text(text1)
words_set2 = clean_text(text2)
result = calculate_similarity(words_set1, words_set2)
print(f"Процент совпадения слов: {result}%")

# set1 = {1,2}
# set2 = {1,2,3,4}
#
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
#
# # for item in set2:
# #     print(item)
#
# squares = {x**2 for x in range(1,6)}
# print(squares)

# # Объединение (union() или |)
# union_set = set1 | set2 #set1.union(set2)
# print(union_set)
#
# # Пересечение (intersection() или &)
# intersection_set = set1 & set2 #set1.intersection(set2)
# print(intersection_set)
#
# # Разность (difference() или -)
# difference_set = set1 - set2 #set1.difference(set2)
# print(difference_set)
#
# # Симметрическая разность (symmetric_difference() или ^)
# symmetric_difference = set1^set2#set1.symmetric_difference(set2)
# print(symmetric_difference)

# my_set = {1,2,3,4,4,5}
# print(my_set)
#
# my_set.add(6)
# print(my_set)
# my_set.add(5)
# print(my_set)

# my_set.remove(3)
# print(my_set)
# my_set.discard(8)
# print(my_set)

# my_set.pop()
# print(my_set)
# my_set.clear()
# print(my_set)


# my_list = [1,2,2,3,4,6,5,6,3]
# unique_set = set(my_list)
# print(unique_set)
#
# empty_set = set()

