"""
Сортировка массива из 0 и 1

Дан массив, содержащий только 0 и 1.
Напишите функцию, которая сортирует его так, чтобы все нули оказались в начале,
а все единички — в конце.
Решение должно быть in-place.
"""


def sort_binary_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr


print(sort_binary_array([0, 1, 1, 0, 1, 0, 1, 0]))
