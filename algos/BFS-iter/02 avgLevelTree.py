from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        ans = []

        queue = deque()
        queue.append(root)

        while queue:

            n = len(queue)
            vals = []

            for i in range(n):

                curr = queue.popleft()
                vals.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            avgval = sum(vals)/len(vals)
            ans.append(avgval)

        return ans
