from heapq import nlargest
from itertools import chain
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        for row, limit in zip(grid, limits):
            candidates.append(nlargest(limit, row))
        
        return sum(nlargest(k, chain.from_iterable(candidates)))

    def maxSum2(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        for row, limit in zip(grid, limits):
            candidates.extend(sorted(row, reverse = True)[:limit])
        
        return sum(sorted(candidates, reverse = True)[:k])