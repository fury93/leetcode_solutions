class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res, mx, maxIdx = 0, max(nums), []

        for i, n in enumerate(nums):
            if n == mx:
                maxIdx.append(i)
            if len(maxIdx) >= k:
                res += maxIdx[-k] + 1
        
        return res