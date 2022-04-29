def insertion_sort(a):

    for i in range(1, len(a)):

        val = a[i]

        while i >= 1 and val < a[i-1]:
            a[i] = a[i-1]
            i -= 1

        a[i] = val

    return a

print(insertion_sort([5,1,2,8,4,7]))
