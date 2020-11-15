#sorting technique used by python in sorted()
#fastest sorting technique
#hybrid technique
#based on insertion sort and bubble sort

RUN = 32

""" insertion_sort function"""

def insertionSort(arr,left,right):
    for i in range(left+1, right,1):
        temp = arr[i]
        j = i-1
        while(arr[j]>temp and j>= left):
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = temp

"""merge function"""
def merge(arr,l,m,r):
    len1 = m - l + 1
    len2 = r - m
    left = []
    right = []
    for i in range(0, len1, 1):
        left.append(arr[l + i])
    for i in range(0, len2, 1):
        right.append(arr[m + 1 + i])

    i = 0
    j = 0
    k = l

    while (i < len1 and j < len2):
        if (left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while (i < len1):
        arr[k] = left[i]
        k += 1
        i += 1

    while (j < len2):
        arr[k] = right[j]
        k += 1
        j += 1

""" tim_sort function"""
def tim_sort(arr,n):
    for i in range(0,n,RUN):
        insertionSort(arr, i, min((i + 31), (n - 1)))

    size = RUN
    while(size<n):
        left = 0
        while(left < n):
            mid = left + size-1
            right = min((left + 2*size - 1), (n-1))
            merge(arr, left, mid, right)
            left +=2*size
        size = 2*size

"""main function"""
if __name__ == "__main__":
    list1 = [1,3,5,7,8,5,3,1,0]
    tim_sort(list1,len(list1)+1)
    print(list1)
