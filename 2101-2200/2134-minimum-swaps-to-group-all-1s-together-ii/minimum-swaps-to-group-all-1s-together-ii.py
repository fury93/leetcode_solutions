class Solution:
    def minSwaps2(self, nums: List[int]) -> int:
        ones = sum(nums)
        if ones <= 1: return 0
        
        minSwaps, zeros = ones, 0
        for i in range(len(nums) + ones):
            curNum = nums[i % len(nums)]
            zeros += curNum == 0
            if i + 1 < ones: continue
            minSwaps = min(minSwaps, zeros)
            zeros -= nums[(i + 1 - ones) % len(nums)] == 0
        
        return minSwaps

    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        curOnes = maxOnes = sum(nums[:ones])
        
        for i in range(len(nums)):
            curOnes -= nums[i]
            curOnes += nums[(i + ones) % len(nums)]
            maxOnes = max(maxOnes, curOnes)
        
        return ones - maxOnes