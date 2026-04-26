# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def add(node):
            if not node: return True
            carry = add(node.next)
            if carry:
                if node.val < 9:
                    node.val += 1
                    carry = 0
                else:
                    node.val = 0
                    carry = 1
            return carry
        
        if add(head):
            head = ListNode(1, head)
        
        return head
