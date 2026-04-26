# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.res = deque([])
        
        def dfs(node, path):
            if not node: return
            path.appendleft(node.val)
            if not (node.left or node.right):
                if not self.res or path < self.res:
                    self.res = path.copy()
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            path.popleft()

        dfs(root, deque([]))    

        return ''.join(chr(ch + 97) for ch in self.res)