# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        while cur:=prev.next:
            if cur.val < 0:
                prev.next, cur.next, head = cur.next, head, cur
            else:
                prev = cur
        
        return head