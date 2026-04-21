class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        # lcm to get common time for recycle, when none of the drones can work
        r3 = r1 * r2 // math.gcd(r1, r2)
        totalDeliv = sum(d)

        def isEnough(t):
            d1CanDone = t - (t//r1)
            d2CanDone = t - (t//r2)
            d3CanDone = t - (t//r3)

            return d1CanDone >= d1 and d2CanDone >= d2 and d3CanDone >= totalDeliv
            

        l, r = d1 + d2, 2 * (d1 + d2)
        while l < r:
            m = (l+r)//2
            if isEnough(m):
                r = m
            else:
                l = m + 1
            
        return l