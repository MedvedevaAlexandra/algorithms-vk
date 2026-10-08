"""
Развернуть часть массива

Дан массив целых чисел.
Необходимо повернуть (сдвинуть) справа налево часть массива, которая указана
вторым параметром.
Сделать это надо за линейное время без дополнительных аллокаций.

Исходный массив: 1, 2, 3, 4, 5, 6, 7
k = 3
Результат: 5, 6, 7, 1, 2, 3, 4
"""


def reverse_array(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def solution(arr, k):
    if not arr:
        return arr
    n = len(arr)
    k = k % n
    reverse_array(arr, 0, n - 1)
    reverse_array(arr, 0, k - 1)
    reverse_array(arr, k, n - 1)
    return arr


print(solution([1, 2, 3, 4, 5, 6, 7], 3))
