class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapify(nums)
        res = 0
        for i in range(k):
            res -= nums[0]
            heapreplace(nums, nums[0]//3)
        
        return res