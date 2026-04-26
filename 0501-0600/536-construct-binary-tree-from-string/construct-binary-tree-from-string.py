# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        return self._str2treeInternal(s, 0)[0]
    
    def _getNumber(self, s: str, index: int) -> (int, int):
        
        is_negative = False
        
        # A negative number
        if s[index] == '-':
            is_negative = True
            index = index + 1
        
        number = 0
        while index < len(s) and s[index].isdigit():
            number = number * 10 + int(s[index])
            index += 1
        
        return number if not is_negative else -number, index
            
    
    def _str2treeInternal(self, s: str, index: int) -> (TreeNode, int):
        
        if index == len(s):
            return None, index
        
        # Start of the tree will always contain a number representing
        # the root of the tree. So we calculate that first.
        value, index = self._getNumber(s, index)
        node = TreeNode(value)
        
        # Next, if there is any data left, we check for the first subtree
        # which according to the problem statement will always be the left child.
        if index < len(s) and s[index] == '(':
            node.left, index = self._str2treeInternal(s, index + 1)
        
        # Indicates a right child
        if node.left and index < len(s) and s[index] == '(':
            node.right, index = self._str2treeInternal(s, index + 1)
        
        return node, index + 1 if index < len(s) and s[index] == ')' else index



class Solution2:
    
    def str2tree(self, s: str) -> TreeNode:
        
        if not s:
            return None
        
        root = TreeNode()
        stack = [root]
        
        index = 0
        while index < len(s):
            
            node = stack.pop()

            # NOT_STARTED
            if s[index].isdigit() or s[index] == '-':
                value, index = self._getNumber(s, index)
                node.val = value

                # Next, if there is any data left, we check for the first subtree
                # which according to the problem statement will always be the left child.
                if index < len(s) and s[index] == '(':
                    stack.append(node)

                    node.left = TreeNode()
                    stack.append(node.left)
            
            # LEFT_DONE
            elif node.left and s[index] == '(':
                stack.append(node)

                node.right = TreeNode()
                stack.append(node.right)
            
            index += 1
        return stack.pop() if stack else root
    
    def _getNumber(self, s: str, index: int) -> (int, int):
        
        is_negative = False
        
        # A negative number
        if s[index] == '-':
            is_negative = True
            index = index + 1
        
        number = 0
        while index < len(s) and s[index].isdigit():
            number = number * 10 + int(s[index])
            index += 1
        
        return number if not is_negative else -number, index