class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        dp = [0] * (budget+1)
        for p, f in zip(present, future):
            for j in range(budget, p-1, -1):
                dp[j] = max(dp[j], dp[j-p] + f-p)
        return dp[-1]

class Solution2:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        profit_list = []
        for p, f in zip(present, future):
            profit = f - p
            if profit < 0 or p > budget:
                continue
            profit_list.append((profit, p))
        
        dp = [0] *(budget+1)
        for profit, price in profit_list:
            print(profit, price)
            for i in range(budget, price-1, -1):
                dp[i] = max(dp[i], dp[i-price]+profit)
            
        return dp[-1]