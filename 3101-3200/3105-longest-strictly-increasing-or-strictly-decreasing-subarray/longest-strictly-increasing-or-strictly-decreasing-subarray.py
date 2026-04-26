class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def longestIncreasing():
            mx, cur = 0, 1
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    cur += 1
                else:
                    mx = max(mx, cur)
                    cur = 1
            return max(mx, cur)

        def longestDecreasing():
            mx, cur = 0, 1
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                   cur += 1
                else:
                    mx = max(mx, cur)
                    cur = 1
            return max(mx, cur)

        return max(longestIncreasing(), longestDecreasing())