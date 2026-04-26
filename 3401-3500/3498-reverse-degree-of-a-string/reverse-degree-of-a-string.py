class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i, ch in enumerate(s, start = 1):
            code = 26 - (ord(ch) - 97)
            res += i * code
        return res
