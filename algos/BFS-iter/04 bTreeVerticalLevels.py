from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []

        ans = []
        hashtable = defaultdict(list)

        queue = deque()
        queue.append((0, root))

        while queue:

            n = len(queue)

            for i in range(n):

                curr_index, curr = queue.popleft()
                hashtable[curr_index].append(curr.val)

                if curr.left:
                    queue.append((curr_index-1, curr.left))
                if curr.right:
                    queue.append((curr_index+1, curr.right))

        return [x[1] for x in sorted(list(hashtable.items()))]
            
