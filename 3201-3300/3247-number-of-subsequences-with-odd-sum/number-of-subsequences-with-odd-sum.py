class Solution:
    def subsequenceCount(self, nums: List[int], mod = 1_000_000_007) -> int:

        n = len(nums) 

        for num in nums:
            if num %2: break
        else: return 0 
        
        return pow(2, n-1, mod)