# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levels = []  # List to track the last node at each depth
        index, n = 0, len(traversal)

        while index < n:
            # Count depth (number of dashes)
            depth = 0
            while index < n and traversal[index] == "-":
                depth += 1
                index += 1

            # Extract node value
            value = 0
            while index < n and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1

            # Create the new node
            node = TreeNode(value)

            # Adjust levels list to match the current depth
            if depth < len(levels):
                levels[depth] = node
            else:
                levels.append(node)

            # Attach the node to its parent
            if depth > 0:
                parent = levels[depth - 1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

        # The root node is always at index 0
        return levels[0]