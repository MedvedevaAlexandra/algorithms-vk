"""
Развернуть массив

Дан массив целых чисел.
Необходимо развернуть его.
Сделать это надо за линейное время без дополнительных аллокаций.
"""


def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


print(reverse_array([3, 8, 6, 9, 9, 8, 6]))
