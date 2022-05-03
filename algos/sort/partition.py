def naive_partition(a, lo, hi):
    pivot = a[hi]
    left  = [a[i] for i in range(lo,hi) if a[i]<pivot]
    right = [a[i] for i in range(lo,hi) if a[i]>=pivot]
    a[lo:hi+1] = left + [pivot] + right
    return lo + len(left)

def partition_lps(a, lo, hi):

    pivot = a[hi]

    i = lo - 1
    for j in range(lo, hi):
        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[hi] = a[hi], a[i+1]

    return i + 1
