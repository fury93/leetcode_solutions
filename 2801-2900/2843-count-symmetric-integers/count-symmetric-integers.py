class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high+1):
            dig = list(map(int, str(i)))
            L = len(dig)
            if L & 1: continue
            if sum(dig[0:L//2]) == sum(dig[L//2:L]):
                res += 1
        return res