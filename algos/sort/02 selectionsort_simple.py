def selection_sort(a):

    n = len(a)

    for i in range(n - 1):
        min_i = a.index(min(a[i+1:]))
        a[i], a[min_i] = a[min_i], a[i]

    return a

print(selection_sort([5,1,2,8,4,7]))
