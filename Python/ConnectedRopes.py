# Connect Ropes

import heapq 
def minCost(a, n):

    heap = []
    for i in a:
        heapq.heappush(heap, i)
    
    c, m = 0, 0
    while n > 1:
        a = heapq.heappop(heap)
        
        b = heapq.heappop(heap)
        m = a+b
        c = c+m
        heapq.heappush(heap, m)
        n -= 1

    return c

print(minCost([4, 2, 7, 6, 9], 5))


#Another approach without heap
'''
def findMinCost(arr, n):
    l = []
    for each in arr:
        l.append(each)

    cost,sum = 0,0

    while n>1:
        a = min(l)
        l.remove(a)
        
        b = min(l)
        l.remove(b)

        sum = a+b
        cost = cost + sum
        l.append(sum)
        n-=1
    
    return cost
print(findMinCost([4, 3, 2, 6], 4))
'''