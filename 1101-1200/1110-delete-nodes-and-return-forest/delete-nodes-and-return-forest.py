# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res, toDelete = [], set(to_delete)
        
        def dfs(node, isParentDeleted):
            if not node: return None
            isDelete = node.val in toDelete
            if isParentDeleted and not isDelete:
                res.append(node)
            node.left = dfs(node.left, isDelete)
            node.right = dfs(node.right, isDelete)
            return None if isDelete else node
        
        dfs(root, True)
        return res