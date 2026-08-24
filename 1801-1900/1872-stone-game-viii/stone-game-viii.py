class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        for index in range(1, len(stones)):
            stones[index] += stones[index - 1]

        best = stones[-1]
        for index in range(len(stones) - 2, 0, -1):
            best = max(best, stones[index] - best)
        return best

    def stoneGameVIII2(self, stones: List[int]) -> int:
        n = len(stones)
        pre = list(accumulate(stones))
        f = [0] * n
        f[n - 1] = pre[n - 1]
        for i in range(n - 2, 0, -1):
            f[i] = max(f[i + 1], pre[i] - f[i + 1])
        return f[1]