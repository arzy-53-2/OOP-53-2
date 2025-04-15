# Big O нотация

# O(1)

def get_element(arr, index):
    return arr[index]


# print(get_element([1,2,34,5,5,67,8,5,7,8,3,2,4,6,78,2], 6))


# O(log n)

import time

def binary_search(arr, target):
    left, right = 0, len(arr)

    while left <= right:
        mid = (left + right) // 2
        # [1,3,5,7,9,11,13]
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        return -1

# O(n)
# arr = [1,3,5,7,9,11,13]
# target = 7
def find_element(target, arr):
    for value in arr:
        if value == target:
            return value
    return  "Нету"


target = 99999
arr = list(range(199999))

# start_1 = time.time()
# binar = binary_search(target=target, arr=arr)
# end_1 = time.time()
# start_2 = time.time()
# find = find_element(target=target, arr=arr)
# end_2 = time.time()


# print(f"Время выполнения binary: {start_1-end_1:.6f} sek")
# print(f"Время выполнения find: {start_2-end_2:.6f} sek")



# O(n²)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# arr = [5, 1, 4, 2, 8]
#
# print(bubble_sort(arr))

# nums = [2,7,11,15], цель = 9

# O (n2)
target = 9
nums = [2,7,11,15]
def two_sum(nums, target):
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index

print(two_sum(nums, target))
