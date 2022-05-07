# leetcode 99

import binarytree
from collections import deque

tree = [3,1,4,None,None,2]
bTree = binarytree.build(tree)

print(bTree)

def fixTree(root):
    if not root: return

    stack = deque()
    x = y = prev = None

    while stack or root:

        while root:
            stack.append(root)
            root = root.left

        curr = stack.pop()

        if prev and prev.val > curr.val:
            y = curr
            if x is None:
                x = prev
            else:
                break

        prev = curr
        root = curr.right

    x.val, y.val = y.val, x.val

fixTree(bTree)
print(bTree)
