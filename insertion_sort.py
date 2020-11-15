def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i-1
        while j >=0 and val < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
    return arr
print(insertion_sort([1,3,5,7,8,5,3,1,0]))
