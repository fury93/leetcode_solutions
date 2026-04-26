class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res, zeros, ones, L = 0, 0, 0, len(s)
        for i in range(len(s)):
            curIsZero = s[i] == '0'
            zeros += curIsZero
            ones += not curIsZero

            if i == L-1 or s[i] != s[i+1]:
                res += min(zeros, ones)
                if curIsZero: ones = 0
                else: zeros = 0

        return res
