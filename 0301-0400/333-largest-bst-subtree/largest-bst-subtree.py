# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1: Pre-Order Traversal
class Solution:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        """Check if given tree is a valid Binary Search Tree."""
        # An empty tree is a valid Binary Search Tree.
        if not root:
            return True

        # Find the max node in the left subtree of current node.
        left_max = self.find_max(root.left)

        # If the left subtree has a node greater than or equal to the current node,
        # then it is not a valid Binary Search Tree.
        if left_max >= root.val:
            return False

        # Find the min node in the right subtree of current node.
        right_min = self.find_min(root.right)

        # If the right subtree has a value less than or equal to the current node,
        # then it is not a valid Binary Search Tree.
        if right_min <= root.val:
            return False

        # If the left and right subtrees of current tree are also valid BST.
        # then the whole tree is a BST.
        return self.is_valid_bst(root.left) and self.is_valid_bst(root.right)

    def find_max(self, root: Optional[TreeNode]) -> int:
        # Max node in a empty tree should be smaller than parent.
        if not root:
            return float('-inf')
    
        # Check the maximum node from the current node, left and right subtree of the current tree.
        return max(root.val, self.find_max(root.left), self.find_max(root.right))

    def find_min(self, root: Optional[TreeNode]) -> int:
        # Min node in a empty tree should be larger than parent.
        if not root:
            return float('inf')
        
        # Check the minimum node from the current node, left and right subtree of the current tree
        return min(root.val, self.find_min(root.left), self.find_min(root.right))

    def count_nodes(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        # Add nodes in left and right subtree.
        # Add 1 and return total size.
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right) 

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # If current subtree is a validBST, its children will have smaller size BST.
        if self.is_valid_bst(root):
            return self.count_nodes(root)
        
        # Find BST in left and right subtrees of current nodes.
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

# Approach 2: Pre-Order Traversal Optimized
class Solution2:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        """Check if given tree is a valid BST using in-order traversal."""
        # An empty tree is a valid Binary Search Tree.
        if not root:
            return True
        
        # If left subtree is not a valid BST return false.
        if not self.is_valid_bst(root.left):
            return False

        # If current node's value is not greater than the previous 
        # node's value in the in-order traversal return false.
        if self.previous and self.previous.val >= root.val:
            return False

        # Update previous node to current node.
        self.previous = root

        # If right subtree is not a valid BST return false.
        return self.is_valid_bst(root.right)

    # Count nodes in current tree.
    def count_nodes(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        # Add nodes in left and right subtree.
        # Add 1 and return total size.
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
        
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Previous node is initially null.
        self.previous = None

        # If current subtree is a validBST, its children will have smaller size BST.
        if self.is_valid_bst(root):
            return self.count_nodes(root)
        
        # Find BST in left and right subtrees of current nodes.
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

# Approach 3: Post-Order Traversal
# Each node will return min node value, max node value, size
class NodeValue:
    def __init__(self, min_node, max_node, max_size):
        self.max_node = max_node
        self.min_node = min_node
        self.max_size = max_size

class Solution3:
    def largest_bst_subtree_helper(self, root):
        # An empty tree is a BST of size 0.
        if not root:
            return NodeValue(float('inf'), float('-inf'), 0)

        # Get values from left and right subtree of current tree.
        left = self.largest_bst_subtree_helper(root.left)
        right = self.largest_bst_subtree_helper(root.right)
        
        # Current node is greater than max in left AND smaller than min in right, it is a BST.
        if left.max_node < root.val < right.min_node:
            # It is a BST.
            return NodeValue(min(root.val, left.min_node), max(root.val, right.max_node), 
                             left.max_size + right.max_size + 1)
        
        # Otherwise, return [-inf, inf] so that parent can't be valid BST
        return NodeValue(float('-inf'), float('inf'), max(left.max_size, right.max_size))

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        return self.largest_bst_subtree_helper(root).max_size