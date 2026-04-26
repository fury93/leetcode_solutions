# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        level = 0
        while(queue):
            if level % 2:
                l, r = 0, len(queue)-1
                while l < r:
                    queue[l].val, queue[r].val = queue[r].val, queue[l].val
                    l +=1
                    r -=1
            
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level +=1
            
        return root
    
    
    def reverseOddLevels2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def dfs(node1, node2, level):
            if not node1 or not node2:
                return
            if level % 2 != 0:
                node1.val, node2.val = node2.val, node1.val
                
            dfs(node1.left, node2.right, level + 1)
            dfs(node1.right, node2.left, level + 1)
        
        dfs(root.left, root.right, 1)
        return root
