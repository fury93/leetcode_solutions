class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # covered diapason [0: coveredTo)
        patches, coveredTo, i = 0, 1, 0

        while coveredTo <= n:
            if i < len(nums) and nums[i] <= coveredTo:
                coveredTo += nums[i] 
                i += 1
            else:
                coveredTo += coveredTo
                patches += 1

        return patches