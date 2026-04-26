class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        map = set(nums)
        while original in map:
            original *=2
        return original