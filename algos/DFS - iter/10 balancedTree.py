# leetcode 101

import binarytree
from collections import deque

bTree = binarytree.build([1,2,2,3,3,3,3,4,4,4,4,4,4,None,None,5,5])
print(bTree)

def isBalancedTree(root):

    if not root: return True

    
