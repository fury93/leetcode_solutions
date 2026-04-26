class Solution:
    def minimumTime(self, hens: List[int], grains: List[int]) -> int:
        def check(t):
            x = 0
            for h in hens:
                r_reach = t
                if grains[x] < h:
                    l_cost = h - grains[x]
                    if l_cost > t:
                        return False
                    # 1) left to grains[x], return to h, then right
                    # 2) right, return to h, then left to grains[x]
                    # which ever gives maximum right reach
                    r_reach = max(0, t - 2 * l_cost, (t - l_cost) // 2)
                # 
                if h + r_reach >= grains[x]:
                    x = bisect_right(grains, h + r_reach, lo = x)
                    if x == ng:
                        return True
            return False
        
        hens.sort()
        grains.sort()
        nh, ng = len(hens), len(grains)
        l = 0
        r = 2 * (max(grains[-1], hens[-1]) - min(grains[0], hens[0]))
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l