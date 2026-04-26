class Solution:
    def getSum(self, nums: List[int]) -> int:
        ans = nums[0]
        MOD = 10**9 + 7
        
        curr = nums[0]
        left = 0
        prior = 0
        for right in range(1, len(nums)):
            diff = nums[right] - nums[right-1]
            
            if abs(diff) != 1:
                prior = 0
                left = right
                curr = 0
            elif prior != diff:
                    curr = nums[right-1]
                    left = right-1
                    prior = diff
            curr += nums[right] * (right-left+1)
            ans = (ans + curr)  % MOD
        return ans
        
# Doesn't work
class Solution2:
    def getSum(self, nums: List[int]) -> int:
        def getSum(diff):
            res, curSum, i, ln = 0, 0, 0, len(nums) - 1
            while i < ln:
                curSum = nums[i]
                while i < ln and nums[i] + diff == nums[i+1]:
                    curSum += nums[i+1]
                    res += curSum
                    #print(curSum, res)
                    i += 1
                    
                i += 1

            # for i in range(len(nums)):
            #     if i > 0 and nums[i] == nums[i-1] + diff:
            #         curSum += nums[i]
            #     else:
            #         curSum = nums[i]
            #     res += curSum
            return res

        res = getSum(1) + getSum(-1) + sum(nums)
        
        return res % (10**9 + 7)