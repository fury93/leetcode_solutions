# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        # 1->2(slow)->2(fast)->1
        # 1->2->3(slow)->2->1(fast)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 1->2->2(->None)<-1
        # 1->2->3(->None)<-2<-1
        rev = None
        while slow:
            slow.next, slow, rev = rev, slow.next, slow
        
        #print(head, rev)
        
        # check palindrome and reverse linked list
        fast = head
        prev = None
        isPalindrome = True
        while rev:
            if isPalindrome and rev.val != fast.val:
                isPalindrome = False
            rev.next, rev, prev = prev, rev.next, rev
            fast = fast.next
        
        return isPalindrome
            