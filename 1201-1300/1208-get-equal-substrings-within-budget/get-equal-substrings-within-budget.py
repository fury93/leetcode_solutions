class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        diff = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        for r in range(len(s)):
            maxCost -= diff[r]
            if maxCost < 0:
                maxCost += diff[l]
                l += 1
        
        return r - l + 1