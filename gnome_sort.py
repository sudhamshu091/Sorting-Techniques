def gnome_sort(array):
    position = 0
    while(position < len(array)):
        if position == 0 or array[position] >= array[position - 1]:
            position += 1
        else:
            temp = array[position]
            array[position] = array[position - 1]
            array[position - 1] = temp
            position -= 1
    return array
print(gnome_sort([1,3,5,7,8,5,3,1,0]))
