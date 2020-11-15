def counting_sort(array, max):
    m = max + 1
    count = [0] * m

    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return array

print(counting_sort([1,3,5,7,8,5,3,1,0], 8))
