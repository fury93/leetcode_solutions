# the same https://leetcode.com/problems/maximum-array-hopping-score-i/
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        res, maxHeight = 0, 0
        for i in range(len(nums)-1, 0, -1):
            maxHeight = max(maxHeight, nums[i])
            res += maxHeight

        return res
