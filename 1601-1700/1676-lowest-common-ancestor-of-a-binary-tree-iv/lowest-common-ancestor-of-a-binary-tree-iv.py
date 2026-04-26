# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        
        def fn(node):
            """Return LCA of nodes."""
            if not node or node in nodes: return node 
            left, right = fn(node.left), fn(node.right)
            return node if left and right else left or right
        
        return fn(root)