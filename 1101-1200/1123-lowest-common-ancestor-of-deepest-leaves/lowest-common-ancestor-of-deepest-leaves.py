# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node: return (None, depth)
            l = dfs(node.left, depth + 1)
            r = dfs(node.right, depth + 1)

            if l[1] > r[1]:
                return l
            elif l[1] < r[1]:
                return r
            else:
                return (node, l[1])
        
        return dfs(root, 0)[0]
        