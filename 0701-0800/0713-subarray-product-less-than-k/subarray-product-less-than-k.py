class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        res, product, left, right = 0, 1, 0, 0
        
        for right, n in enumerate(nums):
            product *= n
            while product >= k:
                product /= nums[left]
                left += 1
            res += right - left + 1
        
        return res