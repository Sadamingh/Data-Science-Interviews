def naive_partition(a, lo, hi):
    pivot = a[hi]
    left  = [a[i] for i in range(lo,hi) if a[i]<pivot]
    right = [a[i] for i in range(lo,hi) if a[i]>=pivot]
    a[lo:hi+1] = left + [pivot] + right
    return lo + len(left)


def partition_lps(a, lo, hi):

    pivot = a[hi]
    left = lo

    for right in range(lo, hi):
        if a[right] < pivot:
            a[left], a[right] = a[right], a[left]
            left += 1

    a[left], a[hi] = a[hi], a[left]

    return left


def partition_hps(a, lo, hi):

    pivot = a[lo]
    i, j = lo, hi

    while (True):

        while (a[i] < pivot):
            i += 1

        while (a[j] > pivot):
            j -= 1

        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]

        i += 1
        j -= 1
