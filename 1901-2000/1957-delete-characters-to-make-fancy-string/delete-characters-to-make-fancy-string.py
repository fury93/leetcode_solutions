class Solution:
    def makeFancyString(self, s: str) -> str:
        res, L = [], len(s)
        for i in (range(L)):
            if i < L-2 and s[i] == s[i+1] == s[i+2]:
                continue
            res.append(s[i])

        return ''.join(res)