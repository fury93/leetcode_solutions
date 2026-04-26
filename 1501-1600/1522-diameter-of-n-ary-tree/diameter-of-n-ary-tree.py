"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
class Solution:
    def diameter(self, root: 'Node') -> int:
        diameter = 0

        def height(node):
            """ return the height of the node """
            nonlocal diameter

            if len(node.children) == 0:
                return 0

            # select the top two heights
            max_height_1, max_height_2 = 0, 0
            for child in node.children:
                parent_height = height(child) + 1
                if parent_height > max_height_1:
                    max_height_1, max_height_2 = parent_height, max_height_1
                elif parent_height > max_height_2:
                    max_height_2 = parent_height

            # calculate the distance between the two farthest leaves nodes.
            distance = max_height_1 + max_height_2
            diameter = max(diameter, distance)

            return max_height_1

        height(root)
        return diameter

class Solution2:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def maxDepth(node, curr_depth):
            """ return the maximum depth of leaves nodes
                 descending from the current node
            """
            nonlocal diameter

            if len(node.children) == 0:
                return curr_depth
            
            # select the top 2 depths from its children
            max_depth_1, max_depth_2 = curr_depth, 0
            for child in node.children:
                depth = maxDepth(child, curr_depth+1)
                if depth > max_depth_1:
                    max_depth_1, max_depth_2 = depth, max_depth_1
                elif depth > max_depth_2:
                    max_depth_2 = depth

            # calculate the distance between the two farthest leaves nodes
            distance = max_depth_1 + max_depth_2 - 2 * curr_depth
            diameter = max(diameter, distance)

            return max_depth_1

        maxDepth(root, 0)
        return diameter