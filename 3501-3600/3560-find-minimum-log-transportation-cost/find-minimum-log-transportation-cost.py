class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        return k * max(n - k, m - k, 0)

    def minCuttingCost2(self, n: int, m: int, k: int) -> int:
        def getCost(logSize, maxSize):
            cost = 0
            while logSize > maxSize:
                logSize = logSize - maxSize
                cost += logSize * maxSize
            return cost
        
        return getCost(n, k) + getCost(m, k)