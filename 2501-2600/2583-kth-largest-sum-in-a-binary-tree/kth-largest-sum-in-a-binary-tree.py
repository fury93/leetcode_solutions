# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels, queue = [], deque([root])

        while queue and root:
            levelSum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                levelSum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            levels.append(levelSum)
        
        if len(levels) < k: return -1
        levels.sort(reverse = True)
        
        return levels[k-1]
