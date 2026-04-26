class Solution:
    @functools.lru_cache(None)
    def encode(self, s: str) -> str:
        i=(s+s).find(s,1)
        encoded=str(len(s)//i)+'['+self.encode(s[:i])+']' if i<len(s) else s
        splitEncoded=[self.encode(s[:i])+self.encode(s[i:]) for i in range(1,len(s))]
        return min(splitEncoded+[encoded],key=len)

class Solution2:
    def encode(self, s: str) -> str:
        n = len(s)
      
        def count(s, p):
            l = len(p)
            cnt = 0
            while (cnt + 1) * l <= len(s) and s[cnt * l : cnt * l + l] == p:
                cnt += 1
            return cnt
        @cache
        def dp(s):
            n = len(s)
            if n <= 4: return s
            res = s
            for l in range(1, n // 2 + 1):
                pattern = s[:l]
                cnt = 1
                j = l
                while j + l <= n and s[j: j + l] == pattern:
                    cnt += 1
                    j += l
                    tmp = str(cnt) + '[' + dp(pattern) + ']' + dp(s[j:])
                    if len(tmp) < len(res):
                        res = tmp
            res1 = s[0] + dp(s[1:])
            if len(res1) < len(res): res = res1
            return res
         
        return dp(s)

class Solution3:
    def encode(self, s: str) -> str:
        def g(i: int, j: int) -> str:
            t = s[i : j + 1]
            if len(t) < 5:
                return t
            k = (t + t).index(t, 1)
            if k < len(t):
                cnt = len(t) // k
                return f"{cnt}[{f[i][i + k - 1]}]"
            return t

        n = len(s)
        f = [[None] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                f[i][j] = g(i, j)
                if j - i + 1 > 4:
                    for k in range(i, j):
                        t = f[i][k] + f[k + 1][j]
                        if len(f[i][j]) > len(t):
                            f[i][j] = t
        return f[0][-1]
        