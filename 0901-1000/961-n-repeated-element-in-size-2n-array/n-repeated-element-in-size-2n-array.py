class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        k = len(nums) // 2
        for key, val in cnt.items():
            if val == k:
                return key
            