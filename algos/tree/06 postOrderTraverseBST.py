import binarytree

tree = [5, 2, 7, 1, 4, None, 14]
BST = binarytree.build(tree)

print(BST)

def inorder_traverse_tree(node):
    if node is not None:
        inorder_traverse_tree(node.left)
        inorder_traverse_tree(node.right)
        print(node.val)

inorder_traverse_tree(BST)
