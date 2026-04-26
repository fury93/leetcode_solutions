# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def heightOfTree(self, root: Optional[TreeNode]) -> int:
    if not root or (root and root.left and root.left.right and root.left.right.val == root.val):
      return 0
    
    return 1 + max(self.heightOfTree(root.left), self.heightOfTree(root.right))        