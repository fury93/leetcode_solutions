class Solution:
    def checkValidString(self, s: str) -> bool:
        minNeed, maxNeed = 0, 0
        for ch in s:
            if ch == '(':
                minNeed += 1
                maxNeed += 1
            elif ch == ')':
                minNeed -= 1
                maxNeed -= 1
            else:
                minNeed -= 1
                maxNeed += 1
            
            if maxNeed < 0:
                return False
            minNeed = max(minNeed, 0)

        return minNeed == 0