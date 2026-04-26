class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1

        while l <= r:
            # while l < r and nums[l] == nums[l+1]:
            #     l += 1
            # while l < r and nums[r] == nums[r-1]:
            #     r -= 1

            mid = (l + r) // 2
            if nums[mid] == target: return True
            # also can check only mid with left or right
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue

            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False