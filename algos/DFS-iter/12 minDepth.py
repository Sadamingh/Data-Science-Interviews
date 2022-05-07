# leetcode 101

import binarytree
from collections import deque

bTree1 = binarytree.build([3,9,20,None,None,15,7])
bTree2 = binarytree.build([1,2])
bTree3 = binarytree.build([1,None,2])

def minDepth(root):

    if not root: return 0

    min_depth = None

    stack = deque()
    stack.append((1, root))

    while stack:

        curr_depth, curr = stack.pop()

        if curr is None: continue

        if not curr.left and not curr.right:
            if min_depth is None:
                min_depth = curr_depth
            else:
                min_depth = min(min_depth, curr_depth)

        stack.append((curr_depth + 1, curr.right))
        stack.append((curr_depth + 1, curr.left))

    return min_depth

print(minDepth(bTree1))
print(minDepth(bTree2))
print(minDepth(bTree3))
