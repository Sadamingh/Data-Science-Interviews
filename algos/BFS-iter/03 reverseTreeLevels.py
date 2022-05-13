from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []

        ans = []

        queue = deque()
        queue.append(root)

        while queue:

            n = len(queue)
            curr_level = []

            for i in range(n):
                curr = queue.popleft()

                curr_level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            ans.append(curr_level)

        return ans[::-1]
