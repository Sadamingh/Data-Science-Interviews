from mergeTwoSortedArray import mergeTwoSortedArray

def merge_sort(data):

    if len(data) <= 1:
        return data

    else:
        m = len(data) // 2
        left, right = merge_sort(data[0:m]), merge_sort(data[m:])
        return mergeTwoSortedArray(left, right)


######################### Tests #########################
print(merge_sort([]))
print(merge_sort([1]))
print(merge_sort([2, 1]))
print(merge_sort([5,1,2,8,4,7]))
#########################################################
