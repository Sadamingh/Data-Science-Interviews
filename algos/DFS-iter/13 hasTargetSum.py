# leetcode 101

import binarytree
from collections import deque

bTree = binarytree.build([5,4,8,11,None,13,4,7,2,None,None,None,1])

def hasTargetSum(root, targetSum):

    if not root: return False

    stack = deque()
    stack.append((0, root))

    while stack:

        curr_sum, curr = stack.pop()

        if not curr: continue

        if not curr.left and not curr.right:
            if curr_sum + curr.val == targetSum:
                return True

        stack.append((curr_sum + curr.val, curr.right))
        stack.append((curr_sum + curr.val, curr.left))

    return False

print(hasTargetSum(bTree, 22))
