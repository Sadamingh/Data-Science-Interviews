# leetcode 99

import binarytree
from collections import deque

tree = [3,1,4,None,None,2]
bTree1 = binarytree.build(tree)
bTree2 = binarytree.build(tree)
bTree3 = binarytree.build([5, 2, 7, 1, 4, None, 14])

def fixTree(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False

    stack1 = deque()
    stack2 = deque()

    while (stack1 and stack2) or (root1 and root2):

        while root1:
            stack1.append(root1)
            root1 = root1.left

        while root2:
            stack2.append(root2)
            root2 = root2.left

        curr1 = stack1.pop()
        curr2 = stack2.pop()

        if curr1.val != curr2.val:
            return False

        root1 = curr1.right
        root2 = curr2.right

    return True

print(fixTree(bTree1, bTree2))
print(fixTree(bTree1, bTree3))
