class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        L = limit + 1

        # Swapping 0 and 1 doesn't change the count, but can reduce memory (O(one*L))
        if one > zero:
            zero, one = one, zero

        dp0_prev, dp1_prev = [0] * (one + 1), [0] * (one + 1)
        for j in range(1, min(one, limit) + 1):
            dp1_prev[j] = 1

        # Store last L = limit + 1 dp1 rows to access dp1[i-L][j]
        dp1q = deque([dp1_prev[:]])
        for i in range(1, zero + 1):
            dp0, dp1 = [0] * (one + 1), [0] * (one + 1)
            if i <= limit:
                dp0[0] = 1

            for j in range(1, one + 1):
                dp0[j] = (dp0_prev[j] + dp1_prev[j] - (dp1q[0][j] if i >= L else 0)) % mod
                dp1[j] = (dp0[j - 1] + dp1[j - 1] - (dp0[j - L] if j >= L else 0)) % mod

            dp1q.append(dp1[:])
            if len(dp1q) > L:
                dp1q.popleft()

            dp0_prev, dp1_prev = dp0, dp1

        return (dp0_prev[one] + dp1_prev[one]) % mod

class Solution2:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7

        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        for i in range(zero + 1):
            for j in range(one + 1):
                for lastBit in range(2):
                    if i == 0:
                        if lastBit == 0 or j > limit:
                            dp[i][j][lastBit] = 0
                        else:
                            dp[i][j][lastBit] = 1
                    elif j == 0:
                        if lastBit == 1 or i > limit:
                            dp[i][j][lastBit] = 0
                        else:
                            dp[i][j][lastBit] = 1
                    elif lastBit == 0:
                        dp[i][j][lastBit] = dp[i - 1][j][0] + dp[i - 1][j][1]
                        if i > limit:
                            dp[i][j][lastBit] -= dp[i - limit - 1][j][1]
                    else:
                        dp[i][j][lastBit] = dp[i][j - 1][0] + dp[i][j - 1][1]
                        if j > limit:
                            dp[i][j][lastBit] -= dp[i][j - limit - 1][0]
                    dp[i][j][lastBit] %= mod
        return (dp[-1][-1][0] + dp[-1][-1][1]) % mod