class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        return int(num_str.replace('6', '9', 1))