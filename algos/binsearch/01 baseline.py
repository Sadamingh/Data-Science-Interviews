def binsearch(a, target):
    lo = 0
    hi = len(a) - 1
    pivot = (lo + hi) // 2

    while True:

        if lo > hi:
            return lo

        pivot = (lo + hi) // 2

        if a[pivot] > target:
            hi = pivot - 1

        elif a[pivot] < target:
            lo = pivot + 1

        else:
            return pivot + 1


print(binsearch([1, 3, 5, 7, 10], 4))
print(binsearch([1, 3, 4, 5, 7, 10], 4))
