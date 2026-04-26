class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleDigitsSum = doubleDigitsSum = 0
        for n in nums:
            if n < 10:
                singleDigitsSum += n
            else:
                doubleDigitsSum += n

        return singleDigitsSum != doubleDigitsSum