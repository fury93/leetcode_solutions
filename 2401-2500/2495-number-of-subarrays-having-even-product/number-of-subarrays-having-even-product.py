class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        ans = val = 0
        for i, x in enumerate(nums): 
            if not x&1: val = i+1
            ans += val 
        return ans 