# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        A = [[-1] * n for _ in range(m)]
        x, y, dx, dy = 0, 0, 0, 1
        
        while head:
            A[x][y] = head.val
            if A[(x+dx)%m][(y+dy)%n] != -1:
                dx, dy = dy, -dx
            x += dx
            y +=dy
            head = head.next
        
        return A