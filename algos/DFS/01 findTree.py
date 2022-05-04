import binarytree

tree = [2, 1, 3, None, 7, 4, 6, None, None, 6, 5, 8]
bTree = binarytree.build(tree)

print(bTree)

def find_tree(root, target):

    print(root.val, end=", ")

    if root.val == target:
        return True

    elif not root.left or not root.right:

        if root.left:
            return find_tree(root.left, target)
        elif root.right:
            return find_tree(root.right, target)
        else:
            return False

    else:
        return find_tree(root.left, target) or find_tree(root.right, target)


print(find_tree(bTree, 4))
print(find_tree(bTree, 6))
print(find_tree(bTree, 7))
print(find_tree(bTree, 10))
