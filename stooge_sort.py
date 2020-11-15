from math import floor
def stooge_sort(array, i = 0, j = - 1):
    j = len(array) - 1 if j == -1 else j
    if array[i] > array[j]:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
    if j - i + 1 > 2:
        t = floor((j - i + 1) / 3)
        stooge_sort(array, i, j - t)
        stooge_sort(array, i + t, j)
        stooge_sort(array, i, j - t)
    return array
print(stooge_sort([1,3,5,7,8,5,3,1,0]))
