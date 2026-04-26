class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        bucket = [False] * 60 * 24
        def toMinute(time):
            return int(time[:2]) * 60 + int(time[3:])
        
        minMinute, maxMinute = math.inf, -math.inf
        for time in timePoints:
            minute = toMinute(time)
            if bucket[minute]: return 0
            bucket[minute] = True
            minMinute = min(minMinute, minute)
            maxMinute = max(maxMinute, minute)

        # backward distance between 1'st and last minutes
        minTime = 60 * 24 - maxMinute + minMinute
        prevMinute = minMinute 
        for minute in range(minMinute + 1, maxMinute + 1):
            if not bucket[minute]: continue
            minTime = min(minTime, minute - prevMinute)
            prevMinute = minute

        return minTime