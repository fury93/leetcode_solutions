from math import comb
class Solution:
    def countOfArrays(self, n: int, m: int, k: int) -> int:
        o, e, mod = (m+1)//2, m//2, 10**9+7

        res = 0

        # corner case: when there's no even sections (x == 0), all numbers are odd
        if k == 0:
            res += pow(o, n, mod)

        for x in range(1, (n+1-k)//2+1):
            res += comb(x+k-1, x-1) * comb(n-x-k+1, x) \
                    * pow(e, x+k, mod) * pow(o, n-x-k, mod) % mod
        
        return res % mod