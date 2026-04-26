class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        @cache
        def fac(x):
            if x == 1:
                return 1
            return (x * fac(x - 1)) % MOD
        
        @cache
        def ifac(x):
            if x <= 1:
                return 1
            return pow(x, -1, MOD) * ifac(x - 1) % MOD

        @cache
        def cnk(n, k):
            return fac(n) * ifac(k) * ifac(n - k) % MOD
        
        MOD = 1_000_000_007
        ct = Counter(s)
        ma = max(ct.values())
        ans = 0

        for i in range(1, ma + 1):
            cur = 1
            for ch in ct:
                if ct[ch] >= i:
                    x = cnk(ct[ch], i)
                    cur = cur * (x + 1) % MOD
            ans = (ans + cur - 1) % MOD

        return ans