class Solution:
    def minOperations(self, nums: List[int]) -> int:

        dp = [nums.pop()]

        for n in reversed(nums):

            if n >= dp[-1]: dp.append(n)
            
            else: dp[bisect_right(dp, n)] = n

        return len(dp)