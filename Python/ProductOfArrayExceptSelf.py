"""
    Given an Array find the product of array of all index except self

    I/P: [1, 2, 3, 4]
    O/P: [24, 12, 8, 6]
    Explanation:
        index 0=1 [24] 2*3*4
        index 1=2 [12] 1*3*4
        index 2=3 [8] 1*2*4
        index 3=4 [6] 1*2*3
"""


def multiplyList(myList, index_val):
    # Multiply elements one by one
    result = 1
    for x in myList:
        if index_val != myList.index(x):
            result = result * x
    return result


def product_of_array(arr):
    if not arr:
        return
    result = []
    for each in range(len(arr)):
        product = multiplyList(arr, each)
        result.append(product)
    return result


def product_of_array2(arr):
    """
        left[0] = 1
        left[1] = 1 * 1
        left[2] = 1 * 2
        left[3] = 2 * 3

        arr = [4, 3, 2, 1]
        right[0] = 1
        right[1] = 1 * 4
        right[2] = 4 * 3
        right[2] = 12 * 2

        right =  [24, 12, 4, 1]
        left  =  [1, 1, 2, 6]
        left[0] * right[::-1][0] = 24
        left[1] * right[::-1][1] = 12
        left[2] * right[::-1][2] = 8
        left[3] * right[::-1][3] = 6
    """
    n = len(arr)
    left, right = [1] * n, [1] * n
    product_array = []
    # [1,2,3,4]
    # [1,1,1,1]
    for each in range(1, n):
        left[each] = left[each - 1] * arr[each - 1]

    for each in range(1, n):
        right[each] = right[each - 1] * arr[::-1][each - 1]

    for each in range(n):
        product_array.append(left[each] * right[::-1][each])

    return product_array


if __name__ == "__main__":
    array = [1, 2, 3, 4]
    print(product_of_array(array))
    print(product_of_array2(array))