class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        # Queue for BFS. Every element stores [node, parent]
        queue = deque([[root, None]])

        # Traverse Level by Level
        while queue:
            # Nodes in the current level
            n = len(queue)

            # Hash Set to store nodes of the current level
            visited = set()

            # Traverse all nodes in the current level
            for _ in range(n):
                # Pop the node from the queue
                node, parent = queue.popleft()

                # If node.right is already visited, then the node is defective
                if node.right in visited:
                    # Replace the child of the node's parent with null and return the root
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    return root

                # Add node to visited
                visited.add(node)

                # Add child in queue for traversal in next level
                # They won't get popped in this level because of "n"
                # Add the right child first, so that we can explore right to left
                if node.right:
                    queue.append([node.right, node])
                if node.left:
                    queue.append([node.left, node])


class Solution2:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        # Hash Set to store node value of the rightmost branch
        visited = set()

        # Do Reverse Postorder Traversal
        def build_correct_tree(node):
            # If Empty Node, return
            if node is None:
                return None

            # If node.right is already visited, then the node is defective
            # No need to build tree rooted at "node". Replace it with None
            if node.right and node.right.val in visited:
                return None
            
            # Add this node's value to the visited
            visited.add(node.val)

            # Recursively build tree rooted at "node"
            # Build the right subtree first, so that we can explore the right to left
            node.right = build_correct_tree(node.right)
            node.left = build_correct_tree(node.left)

            # Return the root of the built tree
            return node
        
        # Build entire tree
        return build_correct_tree(root)

class Solution3:
    def __init__(self):
        # Hash Set to store node value of rightmost branch
        self.visited = set()

    # Do Reverse Postorder Traversal. Assume input "root" as "node"
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        # If Empty Node, return
        if root is None:
            return None

        # If node.right is already visited, then the node is defective
        # No need to build tree rooted at "node". Replace it with None
        if root.right and root.right.val in self.visited:
            return None
        
        # Add this node's value to the visited
        self.visited.add(root.val)

        # Recursively build tree rooted at "node"
        # Build the right subtree first, so that we can explore right to left
        root.right = self.correctBinaryTree(root.right)
        root.left = self.correctBinaryTree(root.left)

        # Return node of the built tree
        return root