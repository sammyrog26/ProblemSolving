"""
    This function should find the largest element in the input list and return it.

    :param arr: A list of integers.
    :return: The largest element in arr.

    I/P:    [1, 22, 55, 90]
    O/P:    90

    I/P:    [0, 0, -1, -20, 0, -20]
    O/P:    0

    I/P:    [-25, -100, -5, -22, -50]
    O/P:    -5
"""


def largest_in_list(arr):
    # Sort array by size(Bubble sort)
    for i, each in enumerate(arr):
        for j, k in enumerate(arr):
            if k > each:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp

    # Largest value after sorting array will be end of arr/list
    largest = arr[-1]
    return largest


if __name__ == "__main__":
    print(largest_in_list([-25, -100, -5, -22, -50]))