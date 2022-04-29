def insertion_sort(a):

    for i in range(1, len(a)):
        move_forward_if_smaller(i, a)
    return a


def move_forward_if_smaller(i, a):
    val = a[i]
    while i >= 1 and val < a[i-1]:
        a[i] = a[i-1]
        i -= 1
    a[i] = val


print(insertion_sort([5,1,2,8,4,7]))
