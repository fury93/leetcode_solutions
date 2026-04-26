class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res, s, j = 0, 0, 0

        for i, n in enumerate(nums):
            s += n
            while s * (i-j+1) >= k:
                s -= nums[j]
                j+=1
            res += i - j + 1
        
        return res