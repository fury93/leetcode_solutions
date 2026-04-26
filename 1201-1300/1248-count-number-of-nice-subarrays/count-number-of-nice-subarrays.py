class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atLeastK(k, nums) - self.atLeastK(k-1, nums)
        
    def atLeastK(self, k, nums):
        res, l, odd = 0, 0, 0
        for r, n in enumerate(nums):
            odd += n & 1

            while odd > k:
                odd -= nums[l] & 1
                l += 1
            
            res += r - l + 1

        return res

