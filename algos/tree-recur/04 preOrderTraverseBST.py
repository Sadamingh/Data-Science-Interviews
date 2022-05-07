import binarytree

tree = [5, 2, 7, 1, 4, None, 14]
BST = binarytree.build(tree)

def preorder_traverse_tree(node):
    if node is not None:
        print(node.val)
        preorder_traverse_tree(node.left)
        preorder_traverse_tree(node.right)

preorder_traverse_tree(BST)
