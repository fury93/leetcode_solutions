# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node) -> tuple[int, int]:
            if not node: return (0,0)
            inc, dec = 1, 1
            if node.left:
                left = dfs(node.left)
                if node.val == node.left.val + 1:
                    dec += left[1]
                elif node.val == node.left.val - 1:
                    inc += left[0]
            if node.right:
                right = dfs(node.right)
                if node.val == node.right.val + 1:
                    dec = max(dec, right[1] + 1)
                if node.val == node.right.val - 1:
                    inc = max(inc, right[0] + 1)

            self.res = max(self.res, dec + inc - 1)
            return (inc, dec)

        dfs(root)
        return self.res

class Solution2:
    def longestConsecutive(self, root: TreeNode) -> int:
                
        def longest_path(root: TreeNode) -> List[int]:
            nonlocal maxval
            
            if not root:
                return [0, 0]
            
            inr = dcr = 1
            if root.left:
                left = longest_path(root.left)
                if (root.val == root.left.val + 1):
                    dcr = left[1] + 1
                elif (root.val == root.left.val - 1):
                    inr = left[0] + 1
            
            if root.right:
                right = longest_path(root.right)
                if (root.val == root.right.val + 1):
                    dcr = max(dcr, right[1] + 1)
                elif (root.val == root.right.val - 1):
                    inr = max(inr, right[0] + 1)
                    
            maxval = max(maxval, dcr + inr - 1)
            return [inr, dcr]
        
        maxval = 0
        longest_path(root)
        return maxval
            


