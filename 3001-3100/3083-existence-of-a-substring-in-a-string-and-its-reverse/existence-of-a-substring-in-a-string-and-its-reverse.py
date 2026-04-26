class Solution:
    def isSubstringPresent4(self, s: str) -> bool:
        s += ' '
        for i in range(1, len(s)-1):
            if s[i] == s[i-1] or s[i-1] == s[i+1]:
                return True
        return False

    def isSubstringPresent3(self, s: str) -> bool:
        s += ' '
        for prev, cur, nxt in zip(s, s[1:], s[2:]):
            if cur == prev or prev == nxt:
                return True
        return False

    def isSubstringPresent2(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i] == s[i-1] or i + 1 < len(s) and s[i-1] == s[i+1]:
                return True
        return False

    def isSubstringPresent(self, s: str) -> bool:
        def getPairs(s):
            return {s[i-1:i+1] for i in range(1, len(s))}
        return getPairs(s) & getPairs(s[::-1])