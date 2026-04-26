class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1
        
        maxShifted = nums[0]
        isShiftedPart = False
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if isShiftedPart:
                    return False #just one shift is allowed
                else:
                    isShiftedPart = True
            if isShiftedPart and nums[i] > maxShifted:
                    return False

        return True

                
