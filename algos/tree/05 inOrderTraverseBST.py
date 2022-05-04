import binarytree

tree = [5, 2, 7, 1, 4, None, 14]
BST = binarytree.build(tree)

def inorder_traverse_tree(node):
    if node is not None:
        inorder_traverse_tree(node.left)
        print(node.val)
        inorder_traverse_tree(node.right)

inorder_traverse_tree(BST)
