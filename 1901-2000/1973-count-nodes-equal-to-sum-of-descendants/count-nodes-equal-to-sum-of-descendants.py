# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result: int = 0

    def equalToDescendants(self, root: TreeNode | None) -> int:

        def check_equal(node: TreeNode | None) -> int:
            total = 0
            if node.left:
                total += check_equal(node.left)
            if node.right:
                total += check_equal(node.right)
            if node.val == total:
                self.result += 1

            return total + node.val

        check_equal(root)

        return self.result
        
class Solution2:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node: return 0
            sm = dfs(node.left) + dfs(node.right)
            self.res += node.val == sm
            return sm + node.val
        dfs(root)
        return self.res 