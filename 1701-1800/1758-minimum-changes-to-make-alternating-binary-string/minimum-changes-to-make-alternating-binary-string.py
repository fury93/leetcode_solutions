class Solution:
    def minOperations(self, s: str) -> int:
        res = sum(i & 1 == int(n) for i, n in enumerate(s))
        return min(res, len(s) - res)
            