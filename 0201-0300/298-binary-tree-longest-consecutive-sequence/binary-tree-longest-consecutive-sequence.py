# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 1

        def dfs(node, prev, ln):
            if not node: return
            if node.val == prev+1:
                ln += 1
                self.res = max(self.res, ln)
            else:
                ln = 1
            dfs(node.left, node.val, ln)
            dfs(node.right, node.val, ln)

        dfs(root, -math.inf, 0)

        return self.res