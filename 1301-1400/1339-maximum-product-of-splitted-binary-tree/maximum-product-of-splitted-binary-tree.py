# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        
        def dfs(root, total, result):
            if not root:
                return 0
            subtotal = dfs(root.left, total, result)+dfs(root.right, total, result)+root.val
            result[0] = max(result[0], subtotal*(total-subtotal) )
            return subtotal

        result = [0]
        dfs(root, dfs(root, 0, result), result)
        
        return result[0] % MOD