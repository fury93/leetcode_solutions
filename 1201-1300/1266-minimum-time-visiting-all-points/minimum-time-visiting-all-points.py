class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            prev = points[i-1]
            cur = points[i]
            res += max(abs(cur[0] - prev[0]), abs(cur[1] - prev[1]))
        
        return res