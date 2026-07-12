class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        cnt = Counter(nums)
        mid = nums[len(nums)//2]
        return cnt[mid] == 1