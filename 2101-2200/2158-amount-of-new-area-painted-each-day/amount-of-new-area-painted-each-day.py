class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        res, line = [0] * len(paint), [0] * (10**5 + 1)

        for i, (start, end) in enumerate(paint):
            while start < end:
                res[i] += line[start] == 0
                jump = max(start + 1, line[start])
                line[start] = max(end, line[start])
                start = jump

        return res