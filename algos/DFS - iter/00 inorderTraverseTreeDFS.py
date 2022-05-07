import binarytree
from collections import deque

tree = [2, 1, 3, None, 7, 4, 6, None, None, 6, 5, 8]
bTree = binarytree.build(tree)
tree = [5, 2, 7, 1, 4, None, 14]
BST = binarytree.build(tree)

print(bTree)

def traverse_tree(root):

    if not root: return

    stack = deque()

    while stack or root:

        while root:
            stack.append(root)
            root = root.left

        curr = stack.pop()

        print(curr.val, end=",")

        root = curr.right

    print('\n')

traverse_tree(bTree)
traverse_tree(BST)
