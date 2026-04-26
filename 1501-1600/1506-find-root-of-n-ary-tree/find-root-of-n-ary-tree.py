"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        value_sum = 0

        for node in tree:
            # the value is added as a parent node
            value_sum += node.val
            for child in node.children:
                # the value is deducted as a child node.
                value_sum -= child.val

        # the value of the root node is `value_sum`
        for node in tree:
            if node.val == value_sum:
                return node