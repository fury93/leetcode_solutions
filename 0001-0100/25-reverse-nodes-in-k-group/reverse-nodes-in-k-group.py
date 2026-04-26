# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursive 
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        start = end = head
        # find the k-th node (the end node for the current group)
        for _ in range(k):
            if not end: return head # not enough items (< k) => remain the order
            end = end.next
        # reverse the current group with k nodes
        newHead = self.reverse(start, end)
        # after reverse start is the end for the group, link it with the next reversed group
        start.next = self.reverseKGroup(end, k)

        return newHead

    # reverse diapason [start:end), end not inclusive
    def reverse(self, start, end):
        prev = None
        while start != end:
            start.next, start, prev = prev, start.next, start
        return prev # return head node of the reversed group

    # Iterative, I broke it)
    def reverseKGroup2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getGroupEnd(cur, k):
            for _ in range(k):
                if not cur: return head
                cur = cur.next
            return cur

        def reverseGroup(start, end):
            prev, cur, new_group_start = None, start, end.next
            while cur != new_group_start:
                cur.next, cur, prev = prev, cur.next, cur

        def reverse(start, end):
            prev = None
            while start != end:
                start.next, start, prev = prev, start.next, start
            #return prev # return head node of the reversed group
          

        dummy = ListNode()
        prev_group = dummy
        while head:
            group_start = head
            #if not group_end: break # not enough nodes to make a new group
            
            group_end = reverse(group_start, getGroupEnd(head, k)) # reverse the current group
            prev_group.next = group_end # group_end is the start of the reversed group
            prev_group = group_start # group_start is the end of the reversed group
            next_group_start = group_end.next # save link to the next group start
            group_start.next = next_group_start # link current reversed group with the next group
            head = next_group_start # move current point to the start of the next group

        return dummy.next

        