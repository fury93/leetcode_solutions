class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        dp = [0] * (1 << 17)
        dp[0] = 1
        for num in nums:
            for i in range(max_or_value, -1, -1):# For each existing subset, create a new subset by including the current number
                dp[i | num] += dp[i]
            max_or_value |= num

        return dp[max_or_value]