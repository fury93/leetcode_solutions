# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return
            if node.left: dfs(node.left)
            nodes.append(node)
            if node.right: dfs(node.right)
        
        def build(l, r):
            if l > r: return None
            mid = l + (r-l)//2
            root = nodes[mid]
            root.left = build(l, mid-1)
            root.right = build(mid+1, r)
            return root
        
        nodes = []
        dfs(root)
        return build(0, len(nodes)-1)
