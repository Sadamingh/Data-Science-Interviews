def naive_partition(a, lo, hi):
    pivot = a[hi]
    left  = [a[i] for i in range(lo,hi) if a[i]<pivot]
    right = [a[i] for i in range(lo,hi) if a[i]>=pivot]
    a[lo:hi+1] = left + [pivot] + right
    return lo + len(left)
