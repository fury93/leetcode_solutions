class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        res, l, r = 0, 0, len(nums) - 1

        while l < r:
            if nums[l] + nums[r] < target:
                res += r - l
                l += 1
            else:
                r -= 1

        return res
    
    def countPairs2(self, nums: List[int], target: int) -> int:
        res, L = 0, len(nums)
        for i in range(L):
            for j in range(i+1, L):
                if nums[i] + nums[j] < target:
                    res += 1
        return res