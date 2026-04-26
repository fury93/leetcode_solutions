class Solution:
    def minMaxDifference(self, num: int) -> int:
        minVal, maxVal, num = num, num, str(num)
        for c in num:
            if c != '9':
                maxVal = int(num[::].replace(c, '9'))
                break
        
        for c in num:
            if c != '0':
                minVal = int(num[::].replace(c, '0'))
                break

        return maxVal - minVal
        