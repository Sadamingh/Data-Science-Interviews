# leetcode 101

import binarytree
from collections import deque

bTree1 = binarytree.build([3,9,20,None,None,15,7])
bTree2 = binarytree.build([1,2])
bTree3 = binarytree.build([1,None,2])
bTree4 = binarytree.build([3,9,20,None,1,15,7])
bTree5 = binarytree.build([3,9,20,None,1,15,7,None,None,10])

def maxDepth(root):

    if not root: return None

    ans = None
    max_depth = 1
    stack = deque()
    stack.append((max_depth, root))

    while stack:

        curr_depth, curr = stack.pop()

        if not curr: continue

        max_depth = max(curr_depth, max_depth)

        if max_depth == curr_depth:
            ans =curr.val

        stack.append((curr_depth + 1, curr.right))
        stack.append((curr_depth + 1, curr.left))

    return ans

print(maxDepth(bTree1))
print(maxDepth(bTree2))
print(maxDepth(bTree3))
print(maxDepth(bTree4))
print(maxDepth(bTree5))
