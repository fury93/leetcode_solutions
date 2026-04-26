class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        longestSubstring, zeros, ones = 0, 0, 0
        for c in chain(s, '0'):
            if c == '0':
                if ones:
                    longestSubstring = max(longestSubstring, min(zeros, ones))
                    zeros = ones = 0
                zeros += 1
            else:
                ones += 1

        return longestSubstring * 2

    def findTheLongestBalancedSubstring2(self, s: str) -> int:
        res, zeros, ones = 0, 0, 0
        for c in s:
            if c == '0':
                if ones:
                    res = max(res, min(zeros, ones))
                    zeros = ones = 0
                zeros += 1
            else:
                ones += 1
        res = max(res, min(zeros, ones))

        return res * 2