class Solution:
    def rob(self, nums):
        if len(nums) <= 3: return max(nums)

        def robbery(nums, start, end):
            beforePrev = prev = 0
            for i in range(start, end):
                prev, beforePrev = max(prev, beforePrev + nums[i]), prev

            return prev
    
        return max(robbery(nums, 1, len(nums)), robbery(nums, 0, len(nums)-1))