# leetcode 101

import binarytree
from collections import deque

bTree1 = binarytree.build([1,2,2,3,4,4,3])
bTree2 = binarytree.build([1,2,2,None,3,None,3])

def isSymmetricTree(root):

    stack = deque()
    stack.append((root, root))

    while stack:
        node1, node2 = stack.pop()

        if not node1 and not node2:
            continue
        elif not node1 or not node2:
            return False
        elif node1.val != node2.val:
            return False

        stack.append((node1.right, node2.left))
        stack.append((node1.left, node2.right))

    return True

print(isSymmetricTree(bTree1))
print(isSymmetricTree(bTree2))
