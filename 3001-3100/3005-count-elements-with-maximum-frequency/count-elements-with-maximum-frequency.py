class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        maxF = max(cnt.values())

        return sum(f for f in cnt.values() if f == maxF)