class Solution:
    def totalMoney(self, n: int) -> int:
        res, monday = 0, 1
        while n > 0:
            for day in range(min(n, 7)):
                res += monday + day
            n -= 7
            monday += 1
        return res