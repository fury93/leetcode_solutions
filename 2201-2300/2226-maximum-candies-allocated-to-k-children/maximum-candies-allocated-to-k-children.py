class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        S = sum(candies)
        if S < k: return 0 

        l, r = 1, S//k

        def isEnough(p):
            return sum(c//p for c in candies) >= k

        while l < r:
            m = (l+r+1)//2 # to get most right element
            if isEnough(m):
                l = m
            else:
                r = m - 1
        
        return l