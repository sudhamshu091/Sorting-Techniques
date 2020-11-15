def cocktail_shaker_sort(a):
    sorted = False
    while(not sorted):
        sorted = True
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                sorted = False
        for i in range(len(a) - 1, 1, -1):
            if a[i] < a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp
                sorted = False
    return a
print(cocktail_shaker_sort([1,3,5,7,8,5,3,1,0]))
