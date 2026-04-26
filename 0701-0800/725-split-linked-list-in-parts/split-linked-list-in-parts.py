# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur, l = head, 0
        while cur:
            l += 1
            cur = cur.next
        
        groupSize, overSize = divmod(l, k)
        res, cur = [], head
        
        for i in range(k):
            res.append(cur)
            for _ in range(groupSize + (i < overSize) - 1):
                if cur: cur = cur.next
            
            if cur:
                cur.next, cur = None, cur.next

        return res