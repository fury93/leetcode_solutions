class Solution:
     # Bottom-up with a space optimization
    def rob3(self, nums: List[int]) -> int:
        beforePrev = prev = 0
        for money in nums:
            prev, beforePrev = max(prev, beforePrev + money), prev

        return prev
    
    # Bottom-up without optimization
    def rob2(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        money = [None] * len(nums)
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            money[i] = max(money[i-1], money[i-2] + nums[i])

        return money[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        memo = [None] * len(nums)
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        def robToHouse(i):
            if i < 0: return 0
            if memo[i] is None:
                memo[i] = max(robToHouse(i-1), robToHouse(i-2) + nums[i])

            return memo[i]

        return robToHouse(len(nums)-1)