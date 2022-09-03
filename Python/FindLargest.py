"""
Find Largest Integer in a list

    I/P: [1, 22, 55, 90]
    O/P: 90
"""


def largest_integer(arr):
    largest = arr[0]
    for each in arr:
        if each > largest:
            largest = each
    return largest


if __name__ == "__main__":
    l = [0, 0, -1, -20, 0, -20]
    print(largest_integer(l))