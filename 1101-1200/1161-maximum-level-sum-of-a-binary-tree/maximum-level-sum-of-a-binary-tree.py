class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxLevel, level, maxSum, q = 0, 0, -math.inf, deque([root])

        while q:
            sm = 0
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                sm += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            if sm > maxSum:
                maxLevel, maxSum = level, sm
            
        return maxLevel