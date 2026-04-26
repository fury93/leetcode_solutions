# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        if n == 0: return head
        if m == 0: return None
        
        def move(cur, k):
            while k > 0 and cur:
                cur = cur.next
                k -= 1
            return cur
        
        cur = head
        while cur:
            cur = move(cur, m - 1) # pointer should be on last active node, so do m-1
            if cur:
                cur.next = move(cur.next, n)
                cur = cur.next

        return head


