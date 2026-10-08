"""
Минимальный размер подмассива

Дан массив положительных целых чисел nums и положительное целое число target.
Верните подмассив минимальной длины, сумма элементов которого больше или равна
target. Если такого подмассива не существует, верните 0.
"""


def min_sub_array(nums, target):
    min_len = float("inf")
    left = 0
    cur_sum = 0
    for right in range(len(nums)):
        cur_sum += nums[right]
        while cur_sum >= target:
            min_len = min(min_len, right - left + 1)
            cur_sum -= nums[left]
            left += 1
    if min_len == float("inf"):
        return 0
    return min_len


print(min_sub_array([2, 3, 1, 2, 4, 3], 7))
