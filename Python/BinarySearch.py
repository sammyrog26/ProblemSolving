"""
Search the element in an array using Binary Search.
Binary Search Best-case complexity is O(1) where the element is found at the middle index.
The worst-case complexity is O(log2n).

Input:
    [2, 5, 8, 12, 16, 23, 38, 56, 72]
    56
Output:
    7

# Best Case
Input:
    [1,2,3,4,5]
    3
Output:
    2

# Worst Case
Input:
    [1,2,3,4,5]
    8
Output:
    -1

"""


def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    l = [2, 5, 8, 12, 16, 23, 38, 56, 72]
    search_val = 56
    print(binary_search(l, search_val))
