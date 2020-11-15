def odd_even_sort(array):
    sorted = False
    while(not sorted):
        sorted = True
        for i in range(0, len(array) - 1,2):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                sorted = False
        for i in range(1, len(array) - 1, 2):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                sorted = False
    return array
print(odd_even_sort([1,3,5,7,8,5,3,1,0]))
