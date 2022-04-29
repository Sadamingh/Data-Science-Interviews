def insertion_sort(a):

    n = len(a)

    for i in range(1, n):

        j = i - 1
        val = a[i]

        while j >= 0 and val < a[j]:
            a[j+1] = a[j]
            j -= 1

        a[j+1] = val

    return a


print(insertion_sort([5,1,2,8,4,7]))
