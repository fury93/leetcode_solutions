class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res, qualitySum, maxHeap = float('inf'), 0, []

        for ration, q in sorted([(w / q, q) for w, q in zip(wage, quality)]):
            qualitySum += q
            heappush(maxHeap, -q)
            if len(maxHeap) == k:
                res = min(res, qualitySum * ration)
                qualitySum -= -heappop(maxHeap)
        
        return res