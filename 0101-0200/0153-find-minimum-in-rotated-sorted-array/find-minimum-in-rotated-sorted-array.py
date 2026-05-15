class Solution:
    # compare mid with left, [3 1 2], [1,2]
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid] and nums[l] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
    
    # compare mid with right, if right part is sorted, there is no answer (min val), go to left
    # in fully sorted array when we eliminate right part, we don't lose min value, it's on left side
    # when we compare mid with left value, we can eliminate answer, so current logic won't work
    def findMin2(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]