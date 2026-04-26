# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        res, cur = 0, head
        while cur:
            res += 1 if cur.val > cur.next.val else -1
            cur = cur.next.next
        
        if res > 0: return 'Even'
        elif res < 0: return 'Odd'
        return 'Tie'