# not a code by me
def radix_sort(A):
    RADIX = 10
    maxLength = False
    tmp , placement = -1, 1

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(RADIX)]
        for  i in A:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                A[a] = i
                a += 1
        placement *= RADIX
    return A
A = []
n = input("Enter the number of elements you want to sort : ")
n = int(n)
print("Enter the numbers:")
for i in range(0, n):
    num = int(input())
    A.append(num)
print(radix_sort(A))
