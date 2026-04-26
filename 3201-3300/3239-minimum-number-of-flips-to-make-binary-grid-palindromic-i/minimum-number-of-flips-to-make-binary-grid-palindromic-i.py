class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def getFlips(row):
            return sum(row[i] ^ row[~i] for i in range(len(row)//2))

        return min(sum(map(getFlips, grid)), sum(map(getFlips, zip(*grid))))
