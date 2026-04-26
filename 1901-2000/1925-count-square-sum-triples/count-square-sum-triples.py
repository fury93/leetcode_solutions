class Solution:
    def countTriples(self, n: int) -> int:
        res, limit = 0, n*n
        for i in range(1, n):
            for j in range(i+1, n):
                k = i*i + j*j
                if k > limit: break
                if sqrt(k) % 1 == 0:
                    res += 2
                
        return res