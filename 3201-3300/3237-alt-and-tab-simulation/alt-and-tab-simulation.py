class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        res = []
        seen = set()

        for num in queries[::-1]:
            if num in seen:
                continue
            else:
                res.append(num)
                seen.add(num)

        for num in windows:
            if num not in seen:
                res.append(num)
        
        return res