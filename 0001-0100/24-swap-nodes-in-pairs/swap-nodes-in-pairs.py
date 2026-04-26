# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursion
    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            head.next.next, head.next, head = head, self.swapPairs(head.next.next), head.next
        return head
            
    # Iterative
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = last = ListNode(0, head)
        while head and head.next:
            first, second, head = head, head.next, head.next.next
            last.next, last, first.next, second.next = second, first, second.next, first
            
        return dummy.next
        