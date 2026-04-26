class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for start, end in intervals:
            newEnd = min(end, toBeRemoved[0])
            newStart = max(start, toBeRemoved[1])
            
            if start < newEnd:
                res.append([start, newEnd])
            if newStart < end:
                res.append([newStart, end])

        return res
    
    def removeInterval2(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for start, end in intervals:
            if end < toBeRemoved[0] or start > toBeRemoved[1]:
                res.append([start, end])
            else:
                if start < toBeRemoved[0]:
                    res.append([start, toBeRemoved[0]])
                if end > toBeRemoved[1]:
                    res.append([toBeRemoved[1], end])

        return res