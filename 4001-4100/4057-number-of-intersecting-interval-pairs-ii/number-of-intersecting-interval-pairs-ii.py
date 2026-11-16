class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        res = 0

        for i, (_, end) in enumerate(intervals):
            j = bisect_right(intervals, end, key = lambda x: x[0])
            res += j - 1 - i
        
        return res