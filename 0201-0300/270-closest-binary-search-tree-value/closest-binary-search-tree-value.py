# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        while root:
            res = min(res, root.val, key = lambda x: (abs(x - target), x))
            root = root.left if target < root.val else root.right
        return res
   
    
    def closestValue2(self, root: Optional[TreeNode], target: float) -> int:
        res, diff = math.inf, math.inf
        def dfs(node):
            if not node: return
            
            nonlocal res, diff
            curDiff = abs(node.val - target)
            if curDiff < diff:
                res = node.val
                diff = curDiff
            elif curDiff == diff:
                res = min(res, node.val)

            if target < node.val: dfs(node.left)
            else: dfs(node.right)

        dfs(root)

        return res