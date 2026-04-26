class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        dp = [-inf] * (1<<m)
        for num in nums:
            dp[num] = 0
        
        for bit in range(m):
            d = 1<<bit
            for i in range(0,1<<m,d<<1):
                for j in range(i, i+d):
                    if dp[j] < dp[j+d]:
                        dp[j] = dp[j+d]+1
                    elif dp[j] > dp[j+d]:
                        dp[j+d] = dp[j]+1
                    else:
                        dp[j] += 1
                        dp[j+d] += 1
                    
        return [dp[num] for num in nums]