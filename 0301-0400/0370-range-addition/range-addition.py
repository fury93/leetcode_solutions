class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length

        for start, end, diff in updates:
            res[start] += diff
            if end+1 < length:
                res[end+1] -= diff
        
        return list(accumulate(res))