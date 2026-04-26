class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones, zeros = 0, 0
        for ch in s:
            if ch == '1':
                ones += 1
            else:
                zeros += 1
        
        return '1' * (ones-1) + '0' * zeros + '1'