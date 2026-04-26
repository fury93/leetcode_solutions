# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, prev):
            prev = prev + [str(node.val)]
            if not node.left and not node.right:
                self.res += int(''.join(prev), 2)
                return
            if node.left: dfs(node.left, prev)
            if node.right: dfs(node.right, prev)
        
        dfs(root, [])
        return self.res