# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = -math.inf

        def dfs(node):
            if not node: return 0, 0
            leftSum, leftCnt = dfs(node.left)
            rightSum, rightCnt = dfs(node.right)
            curCnt = leftCnt + rightCnt + 1
            curSum = leftSum + rightSum + node.val
            self.res = max(self.res, curSum / curCnt)
            return curSum, curCnt
        
        dfs(root)

        return self.res