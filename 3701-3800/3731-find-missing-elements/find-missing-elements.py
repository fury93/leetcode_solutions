class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        uniq = set(nums)
        return [n for n in range(min(nums), max(nums)) if n not in uniq]
