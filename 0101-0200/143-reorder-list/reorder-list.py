# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next #stuck1
        
        #find middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #inverse list from the middle to the end
        second = slow.next #stuck 2
        slow.next = prev = None #broke relation between first and second parts
            
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        odd = head
        even = prev #start of the second part in prev
        
        while even: # for 1 elem use even not odd
            odd_next, even_next = odd.next, even.next
            
            odd.next = even
            even.next = odd_next
            
            odd, even = odd_next, even_next  

        