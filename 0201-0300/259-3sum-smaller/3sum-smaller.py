class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        for k in range(len(nums)-2):
            bound = target - nums[k]
            l, r = k + 1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] < bound:
                    res += r - l
                    l += 1
                else:
                    r -= 1
        return res