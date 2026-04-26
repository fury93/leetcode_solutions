# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Save node and visited status. Change visited status to True after first pop from the stack. Push first right, then left child to save correct order
    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [(root, False)]
        while(stack):
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        
        return res

    def postorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res, stack = [], [root] * 2
        while(stack):
            node = stack.pop()
            if stack and node is stack[-1]:
                if node.right:
                    stack += [node.right] * 2
                if node.left:
                    stack += [node.left] * 2     
            else:
                res.append(node.val)      
        
        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []