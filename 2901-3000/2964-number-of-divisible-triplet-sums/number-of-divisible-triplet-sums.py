class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        n = len(nums)
        if n < 3:
            return 0
        ans = 0
        map_ = [0] * d
        map_[ (nums[0] + nums[1]) % d ] = 1
        for k in range(2, n):
            nums[k] %= d
            x = (d - nums[k]) % d
            ans += map_[x]
 
            for l in range(k - 1, -1, -1):
                x = (nums[l] + nums[k]) % d
                map_[x] += 1
        return ans 
        
class Solution2:
    def divisibleTripletCount(self, A: List[int], d: int) -> int:
        ans = 0
        for i in range(len(A)):
            seen = Counter()
            for j in range(i+1, len(A)):
                ans += seen[-A[j]%d]
                seen[(A[i]+A[j])%d] += 1
        return ans