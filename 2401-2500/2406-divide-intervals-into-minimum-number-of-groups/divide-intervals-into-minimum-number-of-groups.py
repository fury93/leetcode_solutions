class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        
        res, group, i, j = 0, 0, 0, 0
        while i < len(starts):
            if starts[i] <= ends[j]:
                group += 1
                res = max(res, group)
                i += 1
            else:
                group -= 1
                j += 1
        
        return res