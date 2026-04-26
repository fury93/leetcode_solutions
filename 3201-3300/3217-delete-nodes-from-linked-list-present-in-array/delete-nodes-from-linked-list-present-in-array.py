# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove = set(nums)
        dummy = cur = ListNode()
        while head:
            if head.val not in remove:
                cur.next = cur = head
            head = head.next
            cur.next = None

        return dummy.next