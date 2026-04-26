class Solution:
    def moveZeroes2(self, nums: List[int]) -> None:
        snawBall = 0
        for i, n in enumerate(nums):
            if n == 0:
                snawBall += 1
            elif snawBall > 0:
                nums[i], nums[i - snawBall] =  nums[i - snawBall], nums[i]

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1