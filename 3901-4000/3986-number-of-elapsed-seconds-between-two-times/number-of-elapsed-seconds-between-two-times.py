class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def parseTime(time):
            return map(int, time.split(':'))
        
        h1, m1, s1 = parseTime(startTime)
        h2, m2, s2 = parseTime(endTime)

        return (h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1)