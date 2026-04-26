class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for n in range(num1, num2+1):
            s = str(n)
            for i in range(1, len(s)-1):
                if s[i-1] < s[i] > s[i+1] or s[i-1] > s[i] < s[i+1]:
                    res += 1
        
        return res