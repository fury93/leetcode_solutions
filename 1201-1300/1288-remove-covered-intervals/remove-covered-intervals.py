class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res, maxEnd = 0, 0
        
        for start, end in intervals:
            if end > maxEnd:
                res += 1
                maxEnd = end

        return res
        