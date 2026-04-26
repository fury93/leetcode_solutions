class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        sm, mx = sum(ribbons), max(ribbons)
        l, r = mx // k, min(mx, sm //k)

        def isEnough(cutSize, k):
            for size in ribbons:
                k -= size // cutSize
                if k <= 0: return True
            return False
                
        while l < r:
            m = (l + r + 1) // 2
            if isEnough(m, k): l = m
            else: r = m - 1
        
        return l