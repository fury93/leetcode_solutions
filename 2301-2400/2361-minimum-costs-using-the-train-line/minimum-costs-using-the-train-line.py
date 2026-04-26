class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        dpr, dpe, res = 0, expressCost, [0] * n
        
        for i in range(1, n + 1):
            dpr, dpe = min(dpr, dpe) + regular[i - 1],  min(dpr + expressCost, dpe) + express[i - 1]
            res[i - 1] = min(dpr, dpe)
        return res