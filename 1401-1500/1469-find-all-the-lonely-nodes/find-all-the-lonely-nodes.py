# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        
        def dfs(node, isLonely):
            if not node: return
            if isLonely:
                self.res.append(node.val)

            isLonely = bool(node.left) != bool(node.right)
            dfs(node.left, isLonely)
            dfs(node.right, isLonely)
        
        dfs(root, False)

        return self.res
            

