class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        prev_square = prev_no_square = 0
        res = 0
        for num in nums:
            no_square = max(num, num+prev_no_square)
            square = max(num*num, num*num+prev_no_square, num+prev_square)
            res = max(res, square)
            prev_square, prev_no_square = square, no_square
        
        return res