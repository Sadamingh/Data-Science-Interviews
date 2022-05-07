# leetcode 101

import binarytree
from collections import deque

bTree = binarytree.build([1,2,2,3,3,3,3,4,4,4,4,4,4,None,None,5,5])
print(bTree)

def maxDepth(root):
    """
    Can also use the iteration method.
    """
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def isBalancedTree(root):

    if not root:
        return True

    return abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 and isBalancedTree(root.left) and isBalancedTree(root.right)

print(isBalancedTree(bTree))
