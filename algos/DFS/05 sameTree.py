# leetcode 99

import binarytree
from collections import deque

tree = [3,1,4,None,None,2]
bTree1 = binarytree.build(tree)
bTree2 = binarytree.build(tree)
bTree3 = binarytree.build([5, 2, 7, 1, 4, None, 14])
bTree4 = binarytree.build([1])
bTree5 = binarytree.build([1, None, 2])

def sameTree(root1, root2):

    stack = deque()
    stack.append((root1, root2))

    while stack:

        p, q = stack.pop()

        if not p and not q:
            continue
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False

        stack.append((p.right, q.right))
        stack.append((p.left, q.left))

    return True


print(sameTree(bTree1, bTree2))
print(sameTree(bTree1, bTree3))
print(sameTree(bTree4, bTree5))
