class Solution:
    
    def minLargest(self, nums1, nums2):

        incr =  lambda x, y: x + 1 + (x%2 == y%2)

        n1, n2 = len(nums1), len(nums2)
        dp = [[-inf] * (n2+1) for _ in range(n1+1)]

        dp[0][0] = 0
        for i in range(n1): dp[i+1][0] = incr(dp[i][0], nums1[i])
        for j in range(n2): dp[0][j+1] = incr(dp[0][j], nums2[j])
        
        for i,j in product(range(n1), range(n2)):

            dp[i+1][j+1] = min(incr(dp[i][j+1], nums1[i]),
                               incr(dp[i+1][j], nums2[j]))
                    
        return dp[n1][n2]