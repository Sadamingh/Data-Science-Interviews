from partition import partition_hps

def quick_sort(a, low=0, high=None):
    if high is None: high = len(a) - 1

    if low < high:
        pi = partition_hps(a, low, high)
        quick_sort(a, low, pi - 1)
        quick_sort(a, pi + 1, high)

    return a

print(quick_sort([5,1,2,8,4,7]))
