# Given a plot [[1,4], [1,5], [2,5], [3,6], [6,7]]
#    1    2    3
#  /  \  /      \
# 4    5         6
#                 \
#                  7
# Check if two nodes shares the same ancestor
# Case 1 --------------------
# input = 4, 5
# output = True
# Case 2 --------------------
# input = 2, 6
# output = False

from collections import defaultdict

def func(a, i, j):
    ans = []
    hashmap = defaultdict(set)

    for x in a:
        if x[0] not in hashmap: hashmap[x[0]]
        hashmap[x[1]].add(x[0])

    return bool(hashmap[i].intersection(hashmap[i]))

print(func([[1,4], [1,5], [2,5], [3,6], [6,7]], 4, 5))
print(func([[1,4], [1,5], [2,5], [3,6], [6,7]], 2, 6))
