from heapq import *
def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)
    ordered = []
    while heap:
        ordered.append(heappop(heap))
    return ordered

print(heap_sort([1,3,5,7,8,5,3,1,0]))
