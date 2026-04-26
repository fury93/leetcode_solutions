"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray2(self, root: 'Optional[Node]') -> List[int]:
        res, cur = [], root
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    def toArray(self, root: 'Optional[Node]') -> List[int]:
        def convert(node, depth):
            if not node: 
                res = [None] * depth
                return res
            
            res = convert(node.next, depth + 1)
            res[depth] = node.val
            return res

        return convert(root, 0)
        