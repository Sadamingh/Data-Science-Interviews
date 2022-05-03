import bisect

def find(a, target):
    idx = bisect.bisect_left(a, target)
    if a[idx] == target:
        return idx
    else:
        return -1

print(find([1, 3, 5, 7, 10], 4))
print(find([1, 3, 4, 5, 7, 10], 4))
