import binarytree
from collections import deque

tree = [2, 1, 3, None, 7, 4, 6, None, None, 6, 5, 8]
bTree = binarytree.build(tree)

print(bTree)

def find_tree(root, target):

    if not root:
        return

    stack = deque()
    stack.append(root)

    while stack:

        curr = stack.pop()
        print(curr.val, end=", ")

        if target == curr.val:
            return True

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    return False


print(find_tree(bTree, 4))
print(find_tree(bTree, 6))
print(find_tree(bTree, 7))
print(find_tree(bTree, 10))
