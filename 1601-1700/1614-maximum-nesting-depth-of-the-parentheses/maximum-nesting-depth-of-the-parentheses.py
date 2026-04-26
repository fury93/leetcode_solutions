class Solution:
    def maxDepth(self, s: str) -> int:
        depth, res = 0, 0
        for c in s:
            if c == '(':
                depth +=1
                res = max(res, depth)
            elif c == ')':
                depth -=1
        return res