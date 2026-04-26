class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        digit_str = str(digit)
        return sum(str(n).count(digit_str) for n in nums)