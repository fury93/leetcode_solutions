class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        def getMinSum(nums):
            sm, zeros = 0, 0
            for n in nums:
                if n == 0:
                    zeros += 1
                sm += n

            return (sm + zeros, bool(zeros))
        
        sm1, replacing1 = getMinSum(nums1)
        sm2, replacing2 = getMinSum(nums2)
        
        if (not replacing1 and sm1 < sm2) or (not replacing2 and sm2 < sm1):
            return -1

        return max(sm1, sm2)
        
        