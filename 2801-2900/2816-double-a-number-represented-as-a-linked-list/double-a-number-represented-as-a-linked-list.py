class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def double(cur):
            carry = double(cur.next) if cur.next else 0
            carry, cur.val = divmod(cur.val * 2 + carry, 10)
            return carry
        
        carry = double(head)
        if carry:
            head = ListNode(carry, head)
        
        return head
        