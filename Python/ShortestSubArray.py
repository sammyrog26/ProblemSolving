"""
Find the smallest possible length of a (contiguous) sub-array of nums, that has the same degree as nums.

    Input: nums = [1,2,2,3,1]
    Output: 2
    Explanation:
        The input array has a degree of 2 because both elements 1 and 2 appear twice.
        Of the sub-array that have the same degree:
        [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
        The shortest length is 2. So return 2.

    Input: nums = [1,2,2,3,1,4,2]
    Output: 6
    Explanation:
        The degree is 3 because the element 2 is repeated 3 times.
        So [2,2,3,1,4,2] is the shortest sub-array, therefore returning 6.
"""


def findShortestSubArray(arr):
    left, right, count = {}, {}, {}
    for i, each in enumerate(arr):
        if each not in left:
            left[each] = i
        right[each] = i
        count[each] = count.get(each, 0) + 1

    ans = len(arr)
    degree = max(count.values())
    for x in count:
        if count[x] == degree:
            ans = min(ans, right[x] - left[x] + 1)

    return ans


if __name__ == "__main__":
    input_arr = [1, 2, 2, 3, 1, 4, 2]
    print(findShortestSubArray(input_arr))
