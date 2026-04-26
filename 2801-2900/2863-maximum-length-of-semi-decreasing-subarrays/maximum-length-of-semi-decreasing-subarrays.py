class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        for i in range(n):
            if not stack or nums[i] > nums[stack[-1]]:
                stack.append(i)
        ans = 0
        for i in range(n -1, -1, -1):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                ans = max(ans, i - stack[-1] + 1)
                stack.pop(-1)
        return ans