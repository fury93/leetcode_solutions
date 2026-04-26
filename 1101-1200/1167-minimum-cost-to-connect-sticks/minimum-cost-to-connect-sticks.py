class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        res = 0

        while len(sticks) > 1:
            cost = heappop(sticks) + heappop(sticks)
            heappush(sticks, cost)
            res += cost
            
        return res
