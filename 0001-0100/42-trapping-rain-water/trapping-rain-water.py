class Solution:
    def trap(self, h: List[int]) -> int:
        res, stack = 0, []
        for r, rightBound in enumerate(h):
            while stack and h[stack[-1]] < rightBound:
                bar = h[stack.pop()]
                if stack:
                    l, leftBound = stack[-1], h[stack[-1]]
                    minBound = min(rightBound, leftBound)
                    res += (r - l - 1) * (minBound - bar)
            stack.append(r)

        return res
            
    # two pointers    
    def trap2(self, h: List[int]) -> int:
        res, l , r, lMax, rMax = 0, 0, len(h) - 1, 0, 0
        
        if r < 2: return res

        while l < r:
            if h[l] < h[r]:
                lMax = max(lMax, h[l])
                res += lMax - h[l]
                l += 1
            else:
                rMax = max(rMax, h[r])
                res += rMax - h[r]
                r -= 1
        
        return res