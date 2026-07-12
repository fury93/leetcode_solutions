class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        maxRange, maxRangeSum = -1, 0

        for n in nums:
            digits = str(n)
            curRange = int(max(digits)) - int(min(digits))
            if curRange > maxRange:
                maxRange = curRange
                maxRangeSum = n
            elif curRange == maxRange:
                maxRangeSum += n
        
        return maxRangeSum
