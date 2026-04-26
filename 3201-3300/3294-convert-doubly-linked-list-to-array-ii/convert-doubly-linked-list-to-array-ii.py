"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        ans = []
        # move to the head of the list
        while node.prev:
            node = node.prev
        
        # traverse the list and collect Values
        while node:
            ans.append(node.val)
            node = node.next

        return ans
        
class Solution2:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        res, cur = deque(), node
        while cur.prev:
            cur = cur.prev
            res.appendleft(cur.val)

        cur = node
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        return res
    
    def toArray2(self, node: 'Optional[Node]') -> List[int]:
        while node.prev:
            node = node.prev

        while node:
            yield node.val
            node = node.next