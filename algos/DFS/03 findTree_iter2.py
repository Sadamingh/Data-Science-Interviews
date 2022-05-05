import binarytree
from collections import deque

tree = [2, 1, 3, None, 7, 4, 6, None, None, 6, 5, 8]
bTree = binarytree.build(tree)

print(bTree)

def find_tree(root, target):

    if not root: return

    stack = deque()

    while stack or root:

        while root:
            stack.append(root)
            root = root.left

        curr = stack.pop()

        if target == curr.val:
            return True

        root = curr.right

    return False


print(find_tree(bTree, 4))
print(find_tree(bTree, 6))
print(find_tree(bTree, 7))
print(find_tree(bTree, 10))
