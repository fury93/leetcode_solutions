class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        def gcd(x,y):
            while y:
                x,y = y,x%y
            return x
        res,cur = 0,1
        for num in nums:
            cur = gcd(cur,num)
            if cur==1:
                cur = num
                res+=1
        return res