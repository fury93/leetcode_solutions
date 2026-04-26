class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        minVal, maxVal, L = min(arr), max(arr), len(arr)
        if minVal == maxVal: return minVal
        step = (maxVal - minVal) // L
        arrSet = set(arr)
        for n in range(minVal, maxVal+1, step):
            if n not in arrSet:
                return n