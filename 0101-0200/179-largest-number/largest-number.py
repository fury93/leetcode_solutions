class Solution:
    def largestNumber(self, nums: List[int]) -> str: 
        nums = "".join(sorted(map(str, nums), key=CustomCompare, reverse = True))
        return nums if nums[0] > "0" else "0"


class CustomCompare:
    def __init__(self, s):
        self.s = s
    def __lt__(self, other) -> bool:
        return self.s + other.s < other.s + self.s