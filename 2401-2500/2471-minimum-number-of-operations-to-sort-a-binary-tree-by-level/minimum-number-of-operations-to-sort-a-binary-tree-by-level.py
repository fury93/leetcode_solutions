# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def swapCount(level):
            d = {k:pos for pos, k in enumerate(sorted(level))}
            res = 0

            for i, n in enumerate(level):
                pos = d[n]
                while pos != i:
                    level[pos], level[i] = level[i], level[pos]
                    pos = d[level[i]]
                    res += 1

            return res

        res, queue = 0, deque([root])
        while queue and root:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left: queue.append(cur.left)    
                if cur.right: queue.append(cur.right) 
            res += swapCount(level)

        return res