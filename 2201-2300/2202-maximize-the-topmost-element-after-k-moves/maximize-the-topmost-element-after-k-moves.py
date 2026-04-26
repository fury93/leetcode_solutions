class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            # [18], k = 3 edge case when only 1 element and odd numbers of operations
            if  len(nums) == 1 and k & 1:
                return -1
            return max(nums)

        maxVal = -1
        # leave one operation to insert max removed element back to the pile
        # [2,3,1], k = 2 => element on position k-1 => 3 can't be topmost
        for i in range(k-1):
            maxVal = max(maxVal, nums[i])

        # [1,2,3], k = 2 => 3 is the topmost element and we didn't remove it
        if k < len(nums):
            maxVal = max(maxVal, nums[k])

        return maxVal


