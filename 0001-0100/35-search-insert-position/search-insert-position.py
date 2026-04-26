class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l

    def searchInsert2(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        
        return l