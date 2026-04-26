# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            nxt = cur.next
            val = gcd(cur.val, cur.next.val)
            node = ListNode(val, cur.next)
            cur.next = node
            cur = nxt
        return head