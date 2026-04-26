class Solution:
    def numberCount(self, a: int, b: int) -> int:
        res = 0
        for n in range(a, b+1):
            digits = str(n)
            res += len(digits) == len(set(digits))
        return res