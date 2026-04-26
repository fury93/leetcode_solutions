class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        data = sorted((d, p) for d, p in zip(difficulty, profit))

        res, i, maxProf, L = 0, 0, 0, len(worker)
        for w in sorted(worker):
            while i < L and w >= data[i][0]:
                maxProf = max(maxProf, data[i][1])
                i += 1
            res += maxProf
        
        return res