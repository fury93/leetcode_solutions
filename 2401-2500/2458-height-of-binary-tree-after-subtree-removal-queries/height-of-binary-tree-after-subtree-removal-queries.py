class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        # Dictionaries to store node depths and heights
        node_depths = {}
        subtree_heights = {}

        # Dictionaries to store the first and second largest heights at each level
        first_largest_height = {}
        second_largest_height = {}

        # Depth-first search to calculate node depths and subtree heights
        def _dfs(node, level):
            if not node:
                return 0

            node_depths[node.val] = level

            # Calculate the height of the current subtree
            left_height = _dfs(node.left, level + 1)
            right_height = _dfs(node.right, level + 1)
            current_height = 1 + max(left_height, right_height)

            subtree_heights[node.val] = current_height

            # Update the largest and second largest heights at the current level
            if current_height > first_largest_height.get(level, 0):
                second_largest_height[level] = first_largest_height.get(
                    level, 0
                )
                first_largest_height[level] = current_height
            elif current_height > second_largest_height.get(level, 0):
                second_largest_height[level] = current_height

            return current_height

        _dfs(root, 0)

        # Process each query
        return [
            node_depths[q]
            + (
                second_largest_height.get(node_depths[q], 0)
                if subtree_heights[q] == first_largest_height[node_depths[q]]
                else first_largest_height.get(node_depths[q], 0)
            )
            - 1
            for q in queries
        ]