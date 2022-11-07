"""
Find Second Largest Integer in a list

    I/P: [1, 22, 55, 90]
    O/P: 55

    I/P:  [0, 0, -1, -20, 0, -20]
    O/P: -1

"""
import sys


def second_largest(arr):
    arr_size = len(arr)
    if not arr or arr_size < 2:
        return
    first = second = -sys.maxsize
    for i in range(arr_size):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    return second


if __name__ == "__main__":
    l = [0, -2, -1, -20, -3, -20]
    print(second_largest(l))