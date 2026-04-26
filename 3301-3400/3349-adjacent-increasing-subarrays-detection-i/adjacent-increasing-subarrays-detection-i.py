class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prevLen, curLen, k2 = 0, 1, k * 2
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                curLen += 1
            else:
                prevLen, curLen = curLen, 1

            if (curLen >= k and prevLen >= k) or curLen == k2:
                return True

        return False    