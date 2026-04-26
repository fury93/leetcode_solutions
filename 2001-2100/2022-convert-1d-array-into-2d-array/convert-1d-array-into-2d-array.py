class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if m * n == len(original):
            for i in range(0, len(original), n):
                res.append(original[i:i+n])

        return res
    
    def construct2DArray2(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        res = [[0 for _ in range(n)] for _ in range(m)]
        for idx, val in enumerate(original):
            res[idx//n][idx%n] = val
        return res