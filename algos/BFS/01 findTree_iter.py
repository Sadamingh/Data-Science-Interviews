import binarytree
from collections import deque

tree = [2, 1, 3, None, 7, 4, 6, None, None, 6, 5, 8]
bTree = binarytree.build(tree)

print(bTree)

def find_tree(root, target):

    if not root:
        return

    queue = deque()
    queue.append(root)

    while queue:

        level_len = len(queue)

        for _ in range(level_len):
            curr = queue.popleft()
            print(curr.val, end=", ")
            # perform search
            if target == curr.val:
                return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    return False

print(find_tree(bTree, 4))
print(find_tree(bTree, 6))
print(find_tree(bTree, 7))
print(find_tree(bTree, 10))
