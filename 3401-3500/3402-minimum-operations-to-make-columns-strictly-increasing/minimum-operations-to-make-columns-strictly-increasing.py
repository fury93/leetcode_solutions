class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        res = 0
        for col in zip(*grid):
            prev = -1
            for cur in col:
                if prev >= cur:
                    newCur = prev + 1
                    res += newCur - cur
                    prev = newCur
                else:
                    prev = cur

        return res
        