class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if i & 1:
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
                if i + 1 < len(nums) and nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        