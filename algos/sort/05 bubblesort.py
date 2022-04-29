def bubble_sort(a):

    n = len(a)

    for _ in range(n):
        for i in range(1, n):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]

    return a

print(bubble_sort([5,1,2,8,4,7]))
