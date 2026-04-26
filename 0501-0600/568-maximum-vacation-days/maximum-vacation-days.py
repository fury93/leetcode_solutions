class Solution:
    def maxVacationDays(self, flights, days):
        NINF = float('-inf')
        N, K = len(days), len(days[0])
        best = [NINF] * N
        best[0] = 0
        
        for t in range(K):
            cur = [NINF] * N
            for i in range(N):
                for j, adj in enumerate(flights[i]):
                    if adj or i == j:
                        cur[j] = max(cur[j], best[i] + days[j][t])
            best = cur
        return max(best)