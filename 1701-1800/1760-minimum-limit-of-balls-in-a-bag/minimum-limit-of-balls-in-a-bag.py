class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)

        def isEnoughSize(size):
            operations = 0
            for n in nums:
                if n <= size: continue
                operations += (n-1)//size
                if operations > maxOperations: return False

            return True

        while l < r:
            m = (l+r)//2
            if isEnoughSize(m):
                r = m
            else:
                l = m + 1
        
        return l