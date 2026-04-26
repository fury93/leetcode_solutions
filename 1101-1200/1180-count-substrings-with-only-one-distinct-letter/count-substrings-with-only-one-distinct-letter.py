class Solution:
    def countLetters(self, s: str) -> int:
        l = 0
        count = 0
        for r, c in enumerate(s):
            while s[l] != c:
                l += 1
            count += r - l + 1
        return count
        
class Solution2:
    def countLetters(self, s: str) -> int:
        sm = 0
        for _, g in groupby(s):
            ln = len(list(g))
            sm += ln * (ln + 1) //2
        return sm