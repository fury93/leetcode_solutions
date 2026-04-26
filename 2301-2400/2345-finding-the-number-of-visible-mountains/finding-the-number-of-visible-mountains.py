class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        n = len(peaks)
        
        # sort by  x-intercept(x-y) of left mountain (ascending) first,
        # and      x-intercept(x+y) of right mountain (descending)
        peaks.sort(key = lambda x: (x[0] - x[1], -(x[0] + x[1])))
        
        count = 0
        maxEnd = -inf
        
        # while iterating peaks, count the number of visible peak
        # which has larger x-intercept of right mountain
        for i, (x, y) in enumerate(peaks):
            if x + y > maxEnd:
                maxEnd = x + y
                
                # we need to consider duplicates -> should not count
                if i < n-1 and peaks[i] == peaks[i+1]: continue
                    
                count += 1
        return count
		
		
class Solution2:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        c = collections.Counter()                           # count frequency for each point
        for x, y in peaks:
            c[(x, y)] += 1
        peaks = sorted(c.keys())                            
        if not peaks: return 0
        def within(pa, pb):                                 # return True if `pb` is within `pa`
            x1, y1 = pa
            x2, y2 = pb 
            b1 = y1 - x1
            b2 = y1 + x1
            return y2 <= x2 + b1 and y2 <= -x2 + b2
        n = len(peaks)
        stack = [tuple(peaks[0])]
        for x, y in peaks[1:]:
            while stack and within([x, y], stack[-1]):      # while previous point is `within` the current point 
                stack.pop()
            if not stack or not within(stack[-1], [x, y]):  # if current point is `within` the previous point
                stack.append((x, y))
        return len([p for p in stack if c[p] == 1])         # eliminate repeats and sort          