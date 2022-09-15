"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
"""


def rotate_array_by_n(arr, k):
    """
    Brute Force
        Time Complexity: O(n**2)
        Space Complexity: O(n)
    """
    if not arr:
        return
    check = 1
    n = len(arr)
    while check <= k:
        last = arr[0]
        for i in range(n - 1):
            arr[i] = arr[i + 1]
        arr[n - 1] = last
        check = check + 1
    return arr


def array_rotate_by_k2(arr, k):
    """
    Method 2
        Time Complexity: O(n)
        Auxilary Space: O(1)
    """
    n = len(arr)
    k = k % n
    result = []
    for i in range(n):
        if i < k:
            result.append(arr[n + i - k])
        else:
            result.append(arr[i - k])
    return result


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate_array_by_n(l, k))
