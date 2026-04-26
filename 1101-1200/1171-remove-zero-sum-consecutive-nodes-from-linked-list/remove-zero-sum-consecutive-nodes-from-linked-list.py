# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0, head)
        d, prefix = dict(), 0
        while cur:
            prefix += cur.val
            d[prefix] = cur
            cur = cur.next

        cur, prefix = dummy, 0
        while cur:
            prefix += cur.val
            cur.next = d[prefix].next
            cur = cur.next

        return dummy.next

    def removeZeroSumSublists2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict()
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next


