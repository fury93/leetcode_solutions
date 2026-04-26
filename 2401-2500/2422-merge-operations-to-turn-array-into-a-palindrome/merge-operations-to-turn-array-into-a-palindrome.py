class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i,j = 0,len(nums)-1
        l,r = nums[i],nums[j]
        res = 0
        while i<j:
            if l<r:
                i+=1
                l+=nums[i]
                res += 1
            elif l>r:
                j-=1
                r+=nums[j]
                res += 1
            else:
                i+=1
                l+=nums[i]
                j-=1
                r+=nums[j]
        return res