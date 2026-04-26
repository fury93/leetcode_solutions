class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if n == 0: return quantities[0]
        
        def isEnough(maxCnt):
            return sum(ceil(q/maxCnt) for q in quantities) <= n

        l, r = 1, max(quantities)
        while l < r:
            mid = (l+r)//2
            if isEnough(mid):
                r = mid
            else:
                l = mid + 1
        
        return l