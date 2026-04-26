class Solution:
    def beautifulPair(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [inf, inf]
        seen = {}
        for i, (x, y) in enumerate(zip(nums1, nums2)): 
            if (x, y) in seen: ans = min(ans, [seen[x, y], i])
            else: seen[x, y] = i 
        if ans != [inf, inf]: return ans
        
        points = sorted(((i, x, y) for i, (x, y) in enumerate(zip(nums1, nums2))), key = lambda x : x[1])
        
        def fn(lo, hi): 
            """Return the minimum distance and the corresponding pair."""
            if lo+1 == hi: return inf, -1, -1
            if lo+2 == hi: 
                delta = abs(points[lo][1]-points[lo+1][1]) + abs(points[lo][2]-points[lo+1][2])
                i, ii = points[lo][0], points[lo+1][0]
                if i > ii: i, ii = ii, i 
            else: 
                mid = lo + hi >> 1
                ld, li, lii = fn(lo, mid)
                rd, ri, rii = fn(mid, hi)
                if (ld, li, lii) < (rd, ri, rii): delta, i, ii = ld, li, lii
                else: delta, i, ii = rd, ri, rii 
                split = points[mid][1]
                strip = sorted((points[k] for k in range(lo, hi) if split - delta <= points[k][1] <= split + delta), key = lambda x : x[2])
                for l, (k, x, y) in enumerate(strip): 
                    for kk, xx, yy in strip[l+1 : l+10]: 
                        cand = abs(x-xx) + abs(y-yy)
                        j, jj = min(k, kk), max(k, kk)
                        if (cand, j, jj) < (delta, i, ii): delta, i, ii = cand, j, jj
            return delta, i, ii
        
        return fn(0, len(nums1))[1:]