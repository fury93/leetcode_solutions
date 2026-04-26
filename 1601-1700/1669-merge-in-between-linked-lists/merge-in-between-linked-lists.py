# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy, beforeA, afterB = ListNode(0, list1), None, None
        cur = dummy
        for i in range(b+1):
            if i == a: beforeA = cur
            cur = cur.next
            
        afterB = cur.next
        beforeA.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = afterB
        
        return dummy.next