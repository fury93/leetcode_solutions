# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = defaultdict(int)
        while head:
            d[head.val] += 1
            head = head.next
        
        cur, nextNode = None, None
        for freq in d.values():
            cur = ListNode(freq, nextNode)
            nextNode = cur
        
        return cur