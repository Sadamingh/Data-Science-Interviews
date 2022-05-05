# Given a plot [[1,4], [1,5], [2,5], [3,6], [6,7]]
#    1    2    3
#  /  \  /      \
# 4    5         6
#                 \
#                  7
# Return the furthest ancestor
# Case 1 --------------------
# input = 7
# output = 3
# Case 2 --------------------
# input = 4
# output = 1

def func(a, target):
    maxVal = max(max(a))
    map = list(range(maxVal+1))

    for p, c in a:
        map[c] = p

    x = map[target]

    while True:
        if target == x:
            return target
        else:
            target = map[x]
            x = map[target]


print(func([[1,4], [1,5], [2,5], [3,6], [6,7], [0,1]], 5))
