class Solution:
    # Bottom-Up (not optimized)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        dayset = set(days)
        
        for i in range(1, len(dp)):
            if i in dayset:
                dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
            else:
                dp[i] = dp[i-1]
        
        return dp[-1]

    # Top-Down
    def mincostTickets3(self, days, costs):
        dayset = set(days)
        @cache
        def dp(day):
            if day < days[0]: return 0
            if day in dayset:
                return min(dp(day - d) + c for d, c in zip([1, 7, 30], costs))
            else:
                return dp(day-1)
        
        return dp(days[-1])

    def mincostTickets2(self, days, costs):
        dayset, durations = set(days), [1, 7, 30]

        @cache
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)