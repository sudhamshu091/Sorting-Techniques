def shell_sort(array):
    inc = len(array) // 2
    while inc:
        for i, j in enumerate(array):
            while i >= inc and array[i - inc] > j:
                array[i] = array[i - inc]
                i -= inc
            array[i] = j
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
list = [1,3,5,7,8,5,3,1,0]
shell_sort(list)
print(list)
