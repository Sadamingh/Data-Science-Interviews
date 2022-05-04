import binarytree

tree = [5, 1, 4, None, None, 3, 6]
bTree = binarytree.build(tree)

def traverse_tree(node):
    if node is not None:
        print(node.val)
        traverse_tree(node.left)
        traverse_tree(node.right)

traverse_tree(bTree)
