class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res, period = 0, 0
        for i in range(len(prices)):
            if i == 0 or prices[i] + 1 != prices[i-1]:
                period = 1
            else:
                period += 1
            res += period
        return res