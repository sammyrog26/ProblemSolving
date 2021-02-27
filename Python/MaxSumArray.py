# MaxSumArray
'''
Set Current Value as array[0]
for each iteration:
    find max(array[i], current+array[i])   i=1    eg: current = max(2, 1+2) = 3

'''

def maxSumArray(n, arr):
    '''
    Find Max Sum of Array
    '''
    tillNow = arr[0]
    current = arr[0]

    for i in range(1, n):
        current = max(arr[i], current+arr[i])
        tillNow = max(tillNow, current)
    return tillNow

print(maxSumArray(5, [1,2,3,-2,5]))