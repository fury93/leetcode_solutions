class Solution:
    def maxSizedArray(self, s: int) -> int:
        def check(n: int) -> int:
            res = 0
            for bit in range(n.bit_length()):
                cnt = n >> bit+1 << bit
                if n & 1<<bit:
                    cnt += n & (1<<bit) - 1
                res += (n**2 - (n-cnt)**2) << bit
            res *= n * (n-1) // 2
            return res
        
        return bisect_right(range(s+1), s, key=check)-1 if s else 1