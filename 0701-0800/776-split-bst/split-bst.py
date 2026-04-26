class Solution:
    def splitBST(
        self, root: Optional[TreeNode], target: int
    ) -> List[Optional[TreeNode]]:
        # Base case: if root is None, return two None values

        if not root:
            return [None, None]

        # If root's value is greater than target,
        # recursively split left subtree
        if root.val > target:
            left = self.splitBST(root.left, target)

            # Attach the right part of the split to root's left subtree
            root.left = left[1]
            return [left[0], root]

        # Otherwise, recursively split right subtree
        else:
            right = self.splitBST(root.right, target)
            # Attach the left part of the split to root's right subtree
            root.right = right[0]
            return [root, right[1]]

class Solution2:
    def splitBST(
        self, root: Optional[TreeNode], target: int
    ) -> List[Optional[TreeNode]]:

        # List to store the two split trees
        ans = [None, None]

        # If root is None, return the empty list
        if not root:
            return ans
        # Stack to traverse the tree and find the split point
        stack = []
        # Find the node with the value closest to the target
        while root:
            stack.append(root)
            if root.val > target:
                root = root.left
            else:
                root = root.right
        # Process nodes in reverse order from the stack to perform the split
        while stack:
            curr = stack.pop()
            if curr.val > target:
                # Assign current node's left child to the subtree
                # containing nodes greater than the target
                curr.left = ans[1]
                # current node becomes the new root of this subtree
                ans[1] = curr
            else:
                # Assign current node's right child to the subtree
                # containing nodes smaller than the target
                curr.right = ans[0]
                # current node becomes the new root of this subtree
                ans[0] = curr
        return ans

class Solution3:
    def splitBST(self, root: TreeNode, target: int) -> list[TreeNode]:
        # Create dummy nodes to hold the split tree parts
        dummy_sm = TreeNode(0)
        cur_sm = dummy_sm
        dummy_lg = TreeNode(0)
        cur_lg = dummy_lg

        # Start traversal from the root
        current = root
        next_node = None

        while current is not None:
            if current.val <= target:
                # Attach the current node to the tree
                # with values less than or equal to the target
                cur_sm.right = current
                cur_sm = current

                # Move to the right subtree
                next_node = current.right

                # Clear the right pointer of current node
                cur_sm.right = None

                current = next_node
            else:
                # Attach the current node to the tree
                # with values greather to the target
                cur_lg.left = current
                cur_lg = current

                # Move to the left subtree
                next_node = current.left

                # Clear the left pointer of current node
                cur_lg.left = None

                current = next_node

        # Return the split parts as a list
        return [dummy_sm.right, dummy_lg.left]