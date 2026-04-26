"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':        
        prev, node = None, leaf
        while node: 
            if node == root:
                if prev == node.right: node.right = None
                else: node.left = None
            else: 
                if prev == node.right: node.right = node.left 
                node.left = node.parent
            node.parent, node, prev = prev, node.parent, node 
        return leaf


class Solution2:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        
        def fn(node, prev=None): 
            """Return updated node."""
            if node == root: 
                if prev == node.left: node.left = None
                else: node.right = None
            else: 
                if prev == node.right: node.right = node.left
                node.left = fn(node.parent, node)
            node.parent = prev
            return node 
        
        return fn(leaf)