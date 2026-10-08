"""
Two sum

Дан отсортированный по возрастанию массив целых чисел и некоторое число target.
Необходимо найти два числа в массиве, которые в сумме дают заданное значение
target, и вернуть их индексы.
"""


def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []


print(two_sum([3, 8, 9, 11, 16, 18, 19, 21], 25))
