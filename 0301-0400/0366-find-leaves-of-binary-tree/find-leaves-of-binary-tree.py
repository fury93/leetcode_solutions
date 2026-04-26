# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            curLevel = max(left, right) + 1
            res[curLevel].append(node.val)
            return curLevel
        
        dfs(root)

        return list(res.values())
        