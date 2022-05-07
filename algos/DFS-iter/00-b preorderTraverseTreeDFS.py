import binarytree
from collections import deque

tree = [2, 1, 3, None, 7, 4, 6, None, None, 6, 5, 8]
bTree = binarytree.build(tree)
tree = [5, 2, 7, 1, 4, None, 14]
BST = binarytree.build(tree)

print(BST)

def traverse_tree(root):

    if not root: return

    stack = deque()
    stack.append(root)
    traversal = deque()

    while stack:

        curr = stack.pop()

        if curr:
            traversal.append(curr.val)
            stack.append(curr.right)
            stack.append(curr.left)

    print(traversal)

traverse_tree(bTree)
traverse_tree(BST)
