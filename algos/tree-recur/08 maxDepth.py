# leetcode 101

import binarytree
from collections import deque

bTree1 = binarytree.build([3,9,20,None,None,15,7])
bTree2 = binarytree.build([1,2])
bTree3 = binarytree.build([1,None,2])

def maxDepth(root):

    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

print(maxDepth(bTree1))
print(maxDepth(bTree2))
print(maxDepth(bTree3))
