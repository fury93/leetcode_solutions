# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node: return True
            isLeft = dfs(node.left) if node.left else True
            isRight = dfs(node.right) if node.right else True
            if (not isLeft or node.left and node.left.val != node.val) or \
                not isRight or node.right and node.right.val != node.val: return False
            self.res += 1
            return True
        dfs(root)
        return self.res

class Solution2:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(node):
            if node is None:
                return True

            isLeftUniValue = dfs(node.left)
            isRightUniValue = dfs(node.right)

            # If both the children form uni-value subtrees, we compare the value of
            # chidrens node with the node value.
            if isLeftUniValue and isRightUniValue:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False
    
                self.count += 1
                return True
            # Else if any of the child does not form a uni-value subtree, the subtree
            # rooted at node cannot be a uni-value subtree.
            return False
        
        dfs(root)
        return self.count

class Solution3:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return True, 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            isLeftUniValue = left[0]
            isRightUniValue = right[0]
            count = left[1] + right[1]
            # If both the children form uni-value subtrees, we compare the value of
            # chidrens node with the node value.
            if isLeftUniValue and isRightUniValue:
                if node.left and node.val != node.left.val:
                    return False, count
                if node.right and node.val != node.right.val:
                    return False, count

                return True, count + 1
            # Else if any of the child does not form a uni-value subtree, the subtree
            # rooted at node cannot be a uni-value subtree.
            return False, count
        
        return dfs(root)[1]