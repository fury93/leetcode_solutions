# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dummy, d, cur = ListNode(0, head), defaultdict(int), head
        while cur:
            d[cur.val] += 1
            cur = cur.next
        
        cur, prev = head, dummy
        while cur:
            if d[cur.val] > 1:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next
        
        