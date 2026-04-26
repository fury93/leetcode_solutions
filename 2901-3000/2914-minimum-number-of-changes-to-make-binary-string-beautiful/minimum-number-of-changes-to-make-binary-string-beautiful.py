class Solution:
    def minChanges(self, s: str) -> int:
        res, i, swap = 0, 0, 0
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            substrLen = j - i + swap
            
            if substrLen & 1:
                res += 1
                swap = 1
            else:
                swap = 0
            
            i = j

        return res