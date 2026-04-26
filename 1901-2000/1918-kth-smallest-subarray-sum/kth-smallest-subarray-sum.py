class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def number_of_subarray_sum_less_than_x(x):
            cnt = cur = j = 0
            for i in range(n):
                cur += nums[i]
                while cur > x:
                    cur -= nums[j]
                    j += 1
                cnt += i - j + 1
            return cnt
        n, low, high = len(nums), min(nums), sum(nums)
        while low <= high:
            mid = (low + high) // 2
            if k <= number_of_subarray_sum_less_than_x(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low