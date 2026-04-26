class Solution:
    def maxDistance(self, positions: List[int], m: int) -> int:
        def isEnough(step):
            balls, curPos = 1, first
            while balls < m:
                minDist = curPos + step
                if minDist > last: break
                curPos = positions[bisect_left(positions, minDist)]
                balls += 1

            return balls == m

        positions.sort()
        
        l, r, first, last = 1, positions[-1]//(m-1), positions[0], positions[-1]
        if m == 2: return last - first

        while l < r:
            mid = (l+r+1)//2
            if isEnough(mid):
                l = mid
            else:
                r = mid - 1
        
        return l