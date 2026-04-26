class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * n
        dp[0] = 0

        increase_stack, decrease_stack = [] * n, [] * n

        for i in range(n):
            while decrease_stack and nums[decrease_stack[-1]] <= nums[i]:
                dp[i] = min(dp[i], dp[decrease_stack.pop()] + costs[i])

            while increase_stack and nums[increase_stack[-1]] > nums[i]:
                dp[i] = min(dp[i], dp[increase_stack.pop()] + costs[i])

            increase_stack.append(i)
            decrease_stack.append(i)

        return dp[-1]
        
class Solution2:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        nse, nge = [n] * n, [n] * n
        maxmono, minmono = [], []
        for index in range(n):
            while maxmono and nums[maxmono[-1]] <= nums[index]:
                nge[maxmono.pop()] = index
            
            while minmono and nums[minmono[-1]] > nums[index]:
                nse[minmono.pop()] = index
            
            maxmono.append(index)
            minmono.append(index)
        
        inf = float("inf") 
        
        @cache
        def dp(position):
            if position == n:
                return inf
            
            current_cost = costs[position] if position > 0 else 0
            if position == n - 1:
                return current_cost
            
            return current_cost + min(dp(nge[position]), dp(nse[position])) 
        return dp(0)