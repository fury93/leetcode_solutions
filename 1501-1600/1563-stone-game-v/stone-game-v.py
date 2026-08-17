class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)

        dp = [[0] * n for _ in range(n)]
        best = [[0] * n for _ in range(n)]

        for i in range(n):
            best[i][i] = stoneValue[i]

        for j in range(1, n):
            mid = j
            total_sum = stoneValue[j]
            right_half = 0

            for i in range(j - 1, -1, -1):
                total_sum += stoneValue[i]

                while (
                    (right_half + stoneValue[mid]) * 2
                    <= total_sum
                ):
                    right_half += stoneValue[mid]
                    mid -= 1

                if right_half * 2 == total_sum:
                    dp[i][j] = best[i][mid]
                elif mid == i:
                    dp[i][j] = 0
                else:
                    dp[i][j] = best[i][mid - 1]

                if mid != j:
                    dp[i][j] = max(
                        dp[i][j],
                        best[j][mid + 1]
                    )

                best[i][j] = max(
                    best[i][j - 1],
                    dp[i][j] + total_sum
                )

                best[j][i] = max(
                    best[j][i + 1],
                    dp[i][j] + total_sum
                )

        return dp[0][n - 1]

    def stoneGameV2(self, stoneValue: List[int]) -> int:
        @lru_cache(None)
        def dfs(left: int, right: int) -> int:
            if left == right:
                return 0

            total = sum(stoneValue[left : right + 1])
            suml = ans = 0
            for i in range(left, right):
                suml += stoneValue[i]
                sumr = total - suml
                if suml < sumr:
                    ans = max(ans, dfs(left, i) + suml)
                elif suml > sumr:
                    ans = max(ans, dfs(i + 1, right) + sumr)
                else:
                    ans = max(ans, max(dfs(left, i), dfs(i + 1, right)) + suml)
            return ans

        n = len(stoneValue)
        return dfs(0, n - 1)