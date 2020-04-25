from selectionSort import *
from random import randint

arr = [randint(-100, 100) for i in range(15)]

print(arr)
arr = selection_simple_sort(arr)
print("Отсортировали простым способом")
print(arr)

arr = [randint(-100, 100) for i in range(15)]
print("========Новый массив=======")
print(arr)
selection_sort(arr)
print("Отсортировали нормальным способом")
print(arr)
