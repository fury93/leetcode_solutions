class Solution:
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        l = bisect_left(nums, target)
        if l == len(nums) or nums[l] != target:
            return res
        r = bisect_right(nums, target) - 1
        return [l, r]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res, L = [-1, -1], len(nums)
        left = self.findMostLeft(nums, target)
        if left == L or nums[left] != target: return res
        right = self.findMostRight(nums, target)
        
        return [left, right]
    
    def findMostLeft(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l

    def findMostRight(self, nums, target):
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        
        return l - 1

