class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = list(itertools.accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1] - self.nums[left] 
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)