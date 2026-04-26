class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nums2 = []
        for n in nums:
            if nums2 and nums2[-1] == n: continue
            nums2.append(n)
        
        res, nums = 0, nums2
        for i in range(1, len(nums) - 1):
            if nums[i-1] < nums[i] > nums[i+1] or nums[i-1] > nums[i] < nums[i+1]:
                res += 1
        
        return res

            
