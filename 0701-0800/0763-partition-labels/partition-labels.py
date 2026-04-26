class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {c: i for i, c in enumerate(s)}

        res, end, start = [], 0, 0
        for i, c in enumerate(s):
            end = max(pos[c], end)
            if i == end:
                res.append(end - start + 1)
                start = end + 1 
        
        return res
