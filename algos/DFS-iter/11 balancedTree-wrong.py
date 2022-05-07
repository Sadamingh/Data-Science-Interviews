# leetcode 101

import binarytree
from collections import deque

bTree = binarytree.build([1,2,2,3,3,3,3,4,4,4,4,4,4,None,None,5,5])
print(bTree)

def isBalancedTree(root):

    min_leaf_depth = 0
    max_leaf_depth = 1

    stack = deque()
    stack.append((1, root))

    while stack:

        curr_depth, curr = stack.pop()

        if not curr: continue

        if not curr.left and not curr.right:
            if not min_leaf_depth:
                min_leaf_depth = curr_depth
            else:
                min_leaf_depth = min(min_leaf_depth, curr_depth)
            max_leaf_depth = max(max_leaf_depth, curr_depth)

        stack.append((curr_depth + 1, curr.right))
        stack.append((curr_depth + 1, curr.left))

    if max_leaf_depth == min_leaf_depth and max_leaf_depth > 2:
        return False

    return max_leaf_depth - min_leaf_depth <= 2

print(isBalancedTree(bTree))
