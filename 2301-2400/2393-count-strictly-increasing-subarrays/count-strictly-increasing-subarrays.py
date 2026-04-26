class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = cnt = 0 
        for i, x in enumerate(nums): 
            if i and nums[i-1] >= nums[i]: cnt = 0
            cnt += 1
            ans += cnt 
        return ans 