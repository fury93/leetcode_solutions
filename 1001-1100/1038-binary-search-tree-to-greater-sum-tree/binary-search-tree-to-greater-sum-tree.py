# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        greaterSum = 0
        def dfs(node):
            if not node: return
            nonlocal greaterSum
            dfs(node.right)
            greaterSum += node.val
            node.val = greaterSum
            dfs(node.left)
        
        dfs(root)

        return root