class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        maxCnt = maxWeight // w
        return min(maxCnt, n * n)

