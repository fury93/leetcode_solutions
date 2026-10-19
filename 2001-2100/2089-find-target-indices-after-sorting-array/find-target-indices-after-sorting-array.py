class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        before, k = 0, 0
        for n in nums:
            if n < target:
                before +=1
            elif n == target:
                k +=1
        return list(range(before, before+ k))