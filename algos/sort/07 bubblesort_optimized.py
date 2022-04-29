def bubble_sort(a):

    n = len(a)
    notSwapped = True

    for k in range(n):
        for i in range(1, n-k):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                notSwapped = False
        if notSwapped: break

    return a

print(bubble_sort([5,1,2,8,4,7]))
