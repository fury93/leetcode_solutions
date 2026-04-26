# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        mini = root.val
        res = 1
        level = 1

        while q:

            total = 0
            for _ in range(len(q)):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if total < mini:
                res = level
                mini = total
            
            level += 1
        
        return res