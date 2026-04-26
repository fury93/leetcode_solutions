class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minN, maxN, minNPos, maxNPos = math.inf, -math.inf, None, None
        for pos, n in enumerate(nums):
            if n < minN:
                minN, minNPos = n, pos
            if n >= maxN:
                maxN, maxNPos = n ,pos
        doubleSwap = 1 if maxNPos < minNPos else 0
        
        return minNPos + len(nums) - 1 - maxNPos - doubleSwap   

class Solution2:
    def minimumSwaps(self, nums: List[int]) -> int:
        mi = min(nums)                                     # find minimum
        idx1 = nums.index(mi)                              # locate the first mi from the left side
        
        nums = [nums[idx1]] + nums[:idx1] + nums[idx1+1:]  # make the swaps & update `nums`
        
        mx = max(nums)                                     # find maximum 
        idx2 = nums[::-1].index(mx)                        # locate the first mx from the right side
        return idx1 + idx2                                 # return total swaps needed