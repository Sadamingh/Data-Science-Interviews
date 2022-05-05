# Given a plot [[1,4], [1,5], [2,5], [3,6], [6,7]]
#    1    2    3
#  /  \  /      \
# 4    5         6
#                 \
#                  7
# output a list of nodes with 0 parents or 1 parents

from collections import defaultdict

def func(a):
    ans = []
    hashmap = defaultdict(set)

    for x in a:
        if x[0] not in hashmap: hashmap[x[0]]
        hashmap[x[1]].add(x[0])

    for x in hashmap:
        if len(hashmap[x]) <= 1:
            ans.append(x)

    return ans

print(func([[1,4], [1,5], [2,5], [3,6], [6,7]]))
