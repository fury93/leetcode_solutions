# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        def dfs(node, k):
            if node.len == 0: return node.val[k-1]
            leftLen = node.left.len or len(node.left.val) if node.left else 0
            if k > leftLen:
                return dfs(node.right, k - leftLen)
            else:
                return dfs(node.left, k)
        
        return dfs(root, k)