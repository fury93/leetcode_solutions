class Solution:
    def maxScore(self, nums: List[int]) -> int:
        res, maxN = 0, 0
        for i in range(len(nums)-1, 0, -1):
            maxN = max(maxN, nums[i])
            res += maxN

        return res

    # Stack
    def maxScore2(self, nums: List[int]) -> int:
        stack = []
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                stack.pop()
            stack.append(i)

        return sum((p2 - p1) * nums[p2] for p1, p2 in pairwise(chain([0], stack)))