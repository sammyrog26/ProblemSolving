"""
Find Target sum indices

    I/P: [1,2,3,6], 5
    O/P: 1,2
    Explanation:
        The sum of indices at 1 and 2 is 2+3=5 which is equal to 5

    I/P: [5,2,1,6,5,4], 9
    O/P: 4,5
    Explanation:
        The sum of indices at 1 and 2 is 2+3=5 which is equal to 5
"""


def target_sum_indices(arr, target):
    target_map = {}
    n = len(arr)
    indice = None
    for each in range(0, n):
        tmp = target - arr[each]
        if tmp in target_map:
            print("Sum of Elements: ", tmp, arr[each], "= %s" % target)
            indice = [target_map[tmp], each]
            break
        target_map[arr[each]] = each
    if not indice:
        return -1
    return indice


if __name__ == "__main__":
    target_sum = 9
    l = [5, 2, 3, 6, 5, 6, 4, 5]
    print(target_sum_indices(l, target_sum))