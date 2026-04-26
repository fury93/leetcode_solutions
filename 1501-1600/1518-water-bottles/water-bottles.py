class Solution:
    def numWaterBottles(self, fullBottles: int, numExchange: int) -> int:
        res = fullBottles
        while fullBottles >= numExchange:
            newFullBottles, fullBottles = divmod(fullBottles, numExchange)
            res += newFullBottles
            fullBottles += newFullBottles
                
        return res
