def selection_sort(list):
    for j in range(len(list) - 1, 0, -1):
        max_num = 0
        for i in range(1, j + 1):
            if list[i] > list[max_num]:
                max_num = i
        list[j], list[max_num] = list[max_num], list[j]
    return list
print(selection_sort([1,3,5,7,8,5,3,1,0]))
