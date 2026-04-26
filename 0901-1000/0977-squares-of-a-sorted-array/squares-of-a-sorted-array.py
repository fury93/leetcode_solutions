class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result, l, r = deque(), 0, len(nums) - 1
        
        while (l <= r):
            left, right = abs(nums[l]), abs(nums[r])
            if(left > right):
                result.appendleft(pow(left,2))
                l += 1
            else:
                result.appendleft(pow(right,2))
                r -= 1
               
        return list(result)