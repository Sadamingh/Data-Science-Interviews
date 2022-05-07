# leetcode 101

import binarytree
from collections import deque

bTree = binarytree.build([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1])

def hasTargetSum(root, targetSum):

    if not root: return []

    ans = []
    stack = deque()
    stack.append(([], root))

    while stack:

        curr_branch, curr = stack.pop()
        curr_branch = curr_branch.copy()

        if not curr:
            continue

        if not curr.left and not curr.right:
            if sum(curr_branch) + curr.val == targetSum:
                ans.append(curr_branch)

        curr_branch.append(curr.val)

        stack.append((curr_branch, curr.right))
        stack.append((curr_branch, curr.left))

    return ans

print(hasTargetSum(bTree, 22))
