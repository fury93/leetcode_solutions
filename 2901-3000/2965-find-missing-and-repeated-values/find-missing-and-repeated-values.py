class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        vals, dup, mis = set(), None, 1
        for val in chain(*grid):
            if val in vals: dup = val
            vals.add(val)
        
        while mis in vals: mis += 1
                
        return [dup, mis]
