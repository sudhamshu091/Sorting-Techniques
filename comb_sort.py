from math import floor
def comb_sort(array, shrink = 1.3):
    gap = len(array)
    sorted = False
    while(not sorted):
        gap = max([floor(gap / shrink), 1])
        sorted = True if gap == 1 else False
        for i in range(len(array) - gap):
            if(array[i] > array[i+gap]):
                temp = array[i]
                array[i] = array[i+gap]
                array[i+gap] = temp
    return array
print(comb_sort([1,3,5,7,8,5,3,1,0]))
