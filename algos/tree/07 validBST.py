import binarytree

def inorder_traverse(node, a):
    if node is not None:
        inorder_traverse(node.left, a)
        a.append(node.val)
        inorder_traverse(node.right, a)

def is_valid_BST(root):
    a = []
    inorder_traverse(root, a)
    if a == sorted(a):
        return True
    else:
        return False

tree = [5, 2, 7, 1, 4, None, 14]
BST = binarytree.build(tree)
print(is_valid_BST(BST))

tree = [5, 1, 4, None, None, 3, 6]
bTree = binarytree.build(tree)
print(is_valid_BST(bTree))
