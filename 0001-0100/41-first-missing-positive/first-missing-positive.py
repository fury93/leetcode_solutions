class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_d = len(nums)+1
        for i, n in enumerate(nums):
            if n <= 0 or n > len(nums):
                nums[i] = max_d

        for _, n in enumerate(nums):
            n = abs(n)
            index = n - 1
            if n < max_d and nums[index] > 0:
                nums[index] *= -1

        for i, n in enumerate(nums, 1):
            if n > 0:
                return i  
        
        return max_d
        