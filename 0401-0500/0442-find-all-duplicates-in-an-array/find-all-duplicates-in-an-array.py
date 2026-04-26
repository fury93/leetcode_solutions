class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            pos = abs(num) - 1
            
            if(nums[pos] > 0):
                nums[pos] = -nums[pos]
            else:
                res.append(pos+1)
        
        return res