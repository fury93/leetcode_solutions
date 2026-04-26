class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        ans = prefix = 0 
        freq = Counter({0 : 1})
        for ch in s:
            if ch == '0': prefix += num2
            else: prefix -= num1
            ans += freq[prefix]
            freq[prefix] += 1
        return ans 