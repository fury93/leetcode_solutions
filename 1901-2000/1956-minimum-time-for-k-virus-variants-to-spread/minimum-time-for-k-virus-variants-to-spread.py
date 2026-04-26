class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:

        def fn(day):
            lines = defaultdict(lambda : defaultdict(int))
            for x, y in points:                
                lines[x+y-day][y-x-day] += 1
                lines[x+y+day][y-x+day] += 0
                lines[x+y-day][y-x+day+1] -= 1 
                lines[x+y+day][y-x-day] += 0 
                lines[x+y+day+1][y-x-day] -= 1 
                lines[x+y-day][y-x+day] += 0
                lines[x+y+day+1][y-x+day+1] += 1
            line = defaultdict(int)
            for xx in sorted(lines):
                for yy, vv in lines[xx].items():
                    line[yy] += vv
                prefix = 0
                for yy in sorted(line):
                    prefix += line[yy] 
                    if prefix >= k and ((xx - yy)%2 == 0 or xx+1 not in lines or prefix+line[yy+1] >= k): return True
            return False
        
        lo, hi = 0, 1_000_000_000
        while lo < hi:
            mid = (lo + hi) // 2
            if fn(mid): hi = mid
            else: lo = mid + 1
        return lo