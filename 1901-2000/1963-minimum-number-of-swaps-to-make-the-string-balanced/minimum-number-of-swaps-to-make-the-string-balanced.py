class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        for ch in s:
            if ch == '[':
                balance += 1
            elif balance > 0:
                balance -= 1
        
        return (balance+1)//2

        
    def minSwaps2(self, s: str) -> int:
        res, s, opened, closed, i, j = 0, list(s), 0, 0, 0, len(s)-1
        for i in range(len(s)):
            if s[i] == '[':
                opened += 1
            else:
                closed += 1

            if opened < closed:
                while j > i and s[j] != '[':
                    j -= 1
                s[i], s[j] = s[j], s[i]
                j -= 1
                opened += 1
                closed -= 1
                res += 1
            #print(i, j, opened, closed, res)
        
        return res



