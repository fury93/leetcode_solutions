class Solution:
    def numberOfSubstrings2(self, s: str) -> int:
        res, l, d = 0, 0, defaultdict(int)
        
        for r, ch in enumerate(s):
            d[ch] += 1
            while len(d) == 3:
                remove = s[l]
                d[remove] -= 1
                if d[remove] == 0:
                    d.pop(remove)
                l += 1
            res += l
        return res

    # no sliding window, save last position
    def numberOfSubstrings(self, s: str) -> int:
        res, d = 0, {c: - 1 for c in 'abc'}
        
        for r, ch in enumerate(s):
            d[ch] = r
            res += min(d.values()) + 1
        return res

    # lee215 solution
    def numberOfSubstrings3(self, s: str) -> int:
        res, l, d = 0, 0, {c: 0 for c in 'abc'}
        
        for r, ch in enumerate(s):
            d[ch] += 1
            while all(d.values()):
                d[s[l]] -= 1
                l += 1
            res += l
        return res

        