class Solution:
    def maxScore(self, s: str) -> int:
        res, ones, zeros = 0, sum(map(int, s)), 0

        for i in range(len(s)-1):
            if s[i] == '1':
                ones -=1
            else:
                zeros +=1
            res = max(res, zeros + ones)
            
        return res
