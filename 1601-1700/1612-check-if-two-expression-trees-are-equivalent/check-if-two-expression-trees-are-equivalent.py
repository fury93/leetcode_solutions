# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        
        dic = collections.Counter()
        
        def dfs(node, sign):
            if not node:
                return
            if node.val == '+':
                dfs(node.left, sign)
                dfs(node.right, sign)
            elif node.val == '-': # for follow-up
                dfs(node.left, sign)
                dfs(node.right, -sign)
            else:
                dic[node.val] += sign
        
        dfs(root1, 1)
        dfs(root2, -1)
        return all(x == 0 for x in dic.values())