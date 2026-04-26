class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for val in arr:
            if val*2 in seen or val/2 in seen:
                return True
            seen.add(val)
        
        return False