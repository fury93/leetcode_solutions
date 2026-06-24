import numpy as np
MOD=10**9 + 7

@lru_cache(None)
def dp(size, n):
    if n==1:
        res = np.zeros((size-1,size-1), dtype=object)
        for i,j in combinations(range(size), 2):
            res[i][size-1-j] = 1
        return res
    x,y = divmod(n, 2)
    res = dp(size, x)
    res = np.matmul(res, res)
    if y: res = np.matmul(res, dp(size, 1))
    for i,j in product(range(size-1),repeat=2):
        res[i][j]%=MOD
    return res

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        return (2*dp(r-l+1, n-1).sum())%MOD
        

class Solution2:
    MOD = 1_000_000_007

    def mul(self, a, b):
        n = len(a)
        m = len(b[0])
        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for k in range(len(a[0])):
                r = a[i][k]
                if r == 0:
                    continue
                for j in range(m):
                    res[i][j] = (res[i][j] + r * b[k][j]) % self.MOD
        return res

    def powMul(self, base, exp, res):
        while exp > 0:
            if exp & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            exp >>= 1
        return res

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        if n == 1:
            return m

        size = 2 * m
        u = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(i):
                u[i][j + m] = 1
            for j in range(i + 1, m):
                u[i + m][j] = 1

        dp = [[1] * size]
        dp = self.powMul(u, n - 1, dp)
        ans = 0
        for i in range(size):
            ans = (ans + dp[0][i]) % self.MOD

        return ans