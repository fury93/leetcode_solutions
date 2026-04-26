class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            char = s[l]
            while l <= r and s[l] == char : l += 1
            while  l <= r and s[r] == char: r -= 1
        return r - l + 1

    def minimumLength2(self, s: str) -> int:
        res = len(s)
        s = [(k, len(list(g))) for k, g in groupby(s)]
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l][0] == s[r][0]:
                res -= s[l][1] + s[r][1]
                l, r = l + 1, r - 1
            else:
                return res

        return 0 if s[l][1] > 1 else 1