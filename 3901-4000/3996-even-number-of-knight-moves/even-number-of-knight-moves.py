class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return sum(start) & 1 == sum(target) & 1