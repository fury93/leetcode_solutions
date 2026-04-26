class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(filter(lambda x: x < k, nums))

        res, l, r = -1, 0, len(nums) - 1
        while l < r:
            sm = nums[l] + nums[r]
            if sm >= k:
                r -= 1
            elif sm < k:
                res = max(res, sm)
                l += 1
        return res

class Solution3:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        answer = -1
        nums.sort()
        for i in range(len(nums)):
            j = bisect_left(nums, k - nums[i], i + 1) - 1
            if j > i:
                answer = max(answer, nums[i] + nums[j])
        return answer

class Solution4:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        answer = -1
        count = [0] * 1001
        for num in nums:
            count[num] += 1
        lo = 1
        hi = 1000
        while lo <= hi:
            if lo + hi >= k or count[hi] == 0:
                hi -= 1
            else:
                if count[lo] > (0 if lo < hi else 1):
                    answer = max(answer, lo + hi)
                lo += 1
        return answer