"""
    This function searches for duplicate entries in an input list of ints or strings and
    reports back all of the duplicates it finds.

    :param arr: The input list.
    :return: An output list containing all of the found duplicates within the input list.

    I/P:    ['carrot', 'potato', 'carrot']
    O/P:    ['carrot']

    I/P:    [1, 3, 5, 7, 3, 7, 10, 12, 12, 1, 8, 4]
    O/P:    [1, 3, 7, 12]

    I/P:    ['apple', 'kiwi', 'melon', 'dragonfruit', 'kiwi', 'lemon', 'melon', 'banana']
    O/P:    ['kiwi', 'melon']

    I/P:    [1, 5, 5, -2, 5, 5, 2]
    O/P:    [5]
"""


def find_duplicates(arr):
    result = []
    temp_l = []
    for each in arr:
        if each not in temp_l:
            temp_l.append(each)
        else:
            result.append(each)
    result = set(result)
    return sorted(result)


if __name__ == "__main__":
    l_val = [1, 5, 5, -2, 5, 5, 2]
    print(find_duplicates(l_val))
