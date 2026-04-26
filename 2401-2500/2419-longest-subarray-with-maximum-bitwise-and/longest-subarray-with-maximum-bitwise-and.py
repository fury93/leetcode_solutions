class Solution:
    # 1 pass, kadane
    def longestSubarray(self, nums: List[int]) -> int:
        maxSubarrayLen, subarrayLen, mx, = 0, 0, -math.inf
        for n in nums:
            if n > mx:
                mx = n
                subarrayLen = maxSubarrayLen = 1
            elif n == mx:
                subarrayLen += 1
                maxSubarrayLen = max(maxSubarrayLen, subarrayLen)
            else:
                subarrayLen = 0
        
        return maxSubarrayLen
    
    # 2 pass
    def longestSubarray2(self, nums: List[int]) -> int:
        maxSubarrayLen, subarrayLen, mx, = 0, 0, max(nums)
        for n in nums:
            if n == mx:
                subarrayLen += 1
                maxSubarrayLen = max(maxSubarrayLen, subarrayLen)
            else:
                subarrayLen = 0
        
        return maxSubarrayLen