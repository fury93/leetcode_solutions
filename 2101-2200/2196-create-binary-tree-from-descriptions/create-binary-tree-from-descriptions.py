class Solution:
    def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        # Maps values to TreeNode pointers
        node_map = {}

        # Stores values which are children in the descriptions
        children = set()

        # Iterate through description to create nodes and set up tree structure
        for description in descriptions:
            # Extract parent value, child value, and whether
            # it is a left child (1) or right child (0)
            parent_value = description[0]
            child_value = description[1]
            is_left = bool(description[2])

            # Create parent and child nodes if not already created
            if parent_value not in node_map:
                node_map[parent_value] = TreeNode(parent_value)
            if child_value not in node_map:
                node_map[child_value] = TreeNode(child_value)

            # Attach child node to parent's left or right branch
            if is_left:
                node_map[parent_value].left = node_map[child_value]
            else:
                node_map[parent_value].right = node_map[child_value]

            # Mark child as a child in the set
            children.add(child_value)

        # Find and return the root node
        for node in node_map.values():
            if node.val not in children:
                return node  # Root node found

        return None  # Should not occur according to problem statement