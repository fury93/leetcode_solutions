class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = maxab = maxa = 0
        for c in nums:
            res = max(res, maxab * c)
            maxab = max(maxab, maxa - c)
            maxa = max(maxa, c)
        return res

    
    def maximumTripletValue2(self, nums: List[int]) -> int:
        res, L = 0, len(nums)
        postfix = list(accumulate(reversed(nums), func=max))[::-1]
        for i in range(L-2):
            for j in range(i+1, L-1):
                if nums[j] < nums[i]:
                    #print(nums[i], nums[j], nums[j+1])
                    res = max(res, (nums[i] - nums[j]) * postfix[j+1])
        
        return res
