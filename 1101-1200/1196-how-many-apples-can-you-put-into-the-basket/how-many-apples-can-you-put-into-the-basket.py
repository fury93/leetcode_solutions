class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        i, limit = 0, 5000
        while i < len(weight) and limit > 0:
            if weight[i] > limit: break
            limit -= weight[i]
            i += 1
        return i