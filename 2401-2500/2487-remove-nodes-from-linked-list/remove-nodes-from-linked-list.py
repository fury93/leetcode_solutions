# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(10**5+1)
        stack = [dummy]

        while head:
            while stack[-1].val < head.val:
                stack.pop()
            stack[-1].next = head
            stack.append(head)
            head = head.next
        
        return stack[0].next
            