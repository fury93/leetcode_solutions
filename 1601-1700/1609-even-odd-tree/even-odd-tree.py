# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root.val & 1: return False
        
        def processNode(node):
            if not node: return True
            nonlocal q, prev
            if evenLevel and (not node.val & 1 or node.val <= prev):
                return False
            if not evenLevel and (node.val & 1 or node.val >= prev):
                return False
            q.append(node)
            prev = node.val
            return True

        q, evenLevel = deque([root]), True
        while q:
            evenLevel = not evenLevel
            prev = -math.inf if evenLevel else math.inf
            for _ in range(len(q)):
                node = q.popleft()
                if not processNode(node.left) or not processNode(node.right): return False  
        return True

