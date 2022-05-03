from partition import naive_partition

def quickSort(a, low=0, high=None):
    if high is None: high = len(a) - 1

    if low < high:
        pi = naive_partition(a, low, high)
        quickSort(a, low, pi - 1)
        quickSort(a, pi + 1, high)

    return a

print(quickSort([5,1,2,8,4,7]))
