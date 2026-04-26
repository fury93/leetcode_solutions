class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        return list(sorted(set(nums), reverse = True)[:k])