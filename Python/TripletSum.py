"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
    and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

    I/P: nums = [-1,0,1,2,-1,-4]
    O/P: [[-1,-1,2],[-1,0,1]]
    Explanation:
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.

    Input: nums = [0,1,1]
    Output: []
    Explanation:
        The only possible triplet does not sum up to 0.

"""


def three_sum(arr):
    triplet_list = []
    for i in range(len(arr)):
        for j in range(1, len(arr) - 1):
            triplet_list.append([arr[i], arr[j], arr[j + 1]])
    triplet_list_set = set(tuple(row) for row in triplet_list)
    result = []
    for each in triplet_list_set:
        sum_count = sum(each)
        if sum_count == 0:
            result.append(list(each))
    return result


def three_sum2(arr):
    """
    Method 2
    """
    result = []
    arr.sort()

    for i, each in enumerate(arr):
        if i > 0 and each == arr[i-1]:
            continue
        left = i+1
        right = len(arr) - 1
        while left < right:
            three_sum_val = each + arr[left] + arr[right]
            if three_sum_val > 0:
                right -= 1
            elif three_sum_val < 0:
                left += 1
            else:
                result.append([each, arr[left], arr[right]])
                left += 1
                while arr[left] == arr[right] and left < right:
                    left += 1
    triplet_list_set = set(tuple(row) for row in result)
    result = [list(val) for val in triplet_list_set]
    return result


if __name__ == "__main__":
    input_list = [-1, 0, 1, 2, -1, -4]

    print(three_sum2(input_list))
