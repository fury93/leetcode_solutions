class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [float("-inf")] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if abs(nums[j] - nums[i]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)

        return -1 if dp[n - 1] < 0 else dp[n - 1]

class Solution2:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        prev, flag, L, res = nums[0], False, len(nums), [-1] * len(nums) 
        res[0] = 0
        
        #for i, n in enumerate(nums[1:], start=1):
        #    print(i, n, L)
        #    if abs(n - prev) <= target:
        #        res +=1
        #        prev = n
        #        if i == L:
        #            print('True')
        #            flag = True
        #print(res, flag)

    
        for i in range(1, L):
            #print(i)
            prev = nums[i]
            for j in range(i-1, -1, -1):
                cur = nums[j]
                if abs(cur - prev) <= target and res[j] > -1:
                    res[i] = max(res[j] + 1, res[i]) 
 
        #return res if (flag and res > 0) else -1
        #if prev == nums[-1] and res > 0:
        #    return res
        #return -1    
        return res[-1]
       
    
        

        