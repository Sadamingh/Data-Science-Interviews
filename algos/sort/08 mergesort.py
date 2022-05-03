from mergeTwoSortedArray import mergeTwoSortedArray

def merge_sort(data):

    if len(data) == 0:
        return []

    elif len(data) == 1:
        return [data[0]]

    elif len(data) == 2:
        if data[0]<data[1]:
            return data
        return [data[1], data[0]]

    else:
        m = len(data) // 2
        left = merge_sort(data[0:m])
        right = merge_sort(data[m:])
        return mergeTwoSortedArray(left, right)

print(merge_sort([]))
print(merge_sort([1]))
print(merge_sort([2, 1]))
print(merge_sort([5,1,2,8,4,7]))
