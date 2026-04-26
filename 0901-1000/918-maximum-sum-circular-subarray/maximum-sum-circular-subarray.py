class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curSum, maxSum, minSum, curMin, curMax = 0, -inf, inf, 0, 0

        for n in nums:
            curSum += n
            # Kadane max
            curMax = max(curMax + n, n)
            maxSum = max(maxSum, curMax)
            # Kadane min
            curMin = min(curMin + n, n)
            minSum = min(minSum, curMin)

        # if all nums are negative
        if curSum == minSum:
            return maxSum

        return max(maxSum, curSum - minSum)
        

    # Lee
    def maxSubarraySumCircular2(self, nums: List[int]) -> int:
        total, maxSum, curMax, minSum, curMin = 0, nums[0], 0, nums[0], 0
        for a in nums:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum