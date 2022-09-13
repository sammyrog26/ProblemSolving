"""
    Find the two subarrays based on an array whose sum is same

    I/P:[1,1,1,1]
    O/P: [[1, 1], [1,1]]

    I/P: [1, 2, 3, 4, 5, 5]
    O/P: [[1,2,3,4], [5, 5]]

    I/P: [1,2,3,4]
    O/P: None

"""


def divide_into_sub_array(arr):
    if not arr:
        return None

    sum_val = sum(l)
    if sum_val % 2 == 1:
        return None

    target_sum = sum_val / 2
    running_sum = 0
    n = len(arr)
    result = []
    for i in range(n):
        running_sum += arr[i]
        if running_sum == target_sum:
            result.append(arr[:i + 1])
            result.append(arr[i + 1:])
            return result


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 5]
    print(divide_into_sub_array(l))
