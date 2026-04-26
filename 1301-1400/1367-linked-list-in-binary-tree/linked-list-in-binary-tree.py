# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def isEqual(treeNode, listNode):
            if not listNode: return True
            if not treeNode or treeNode.val != listNode.val: return False
            return isEqual(treeNode.left, listNode.next) or isEqual(treeNode.right, listNode.next)

        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.val == head.val and isEqual(cur, head):
                    return True
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        
        return False
       

                    
