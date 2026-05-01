class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        res, ln = 0, len(nums)
        sm = nums[-1]
        
        for i in range(ln-2, -1, -1):
            avg = sm // (ln - i - 1)
            res += nums[i] > avg
            sm += nums[i]

        return res