class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        nums.sort()
        d = x - y
        def check(steps):
            sub = steps * y
            idx = bisect.bisect_right(nums, sub)
            cnt = steps
            for i in range(idx, len(nums)):
                cnt -= (nums[i] - sub - 1) // d + 1
                if cnt < 0:
                    return False 
            return True
        l = nums[-1] // x - 1
        r = nums[-1] // y + 1
        while (r - l)>1:
            m = (r+l) //2 
            if check(m):
                r = m 
            else:
                l = m 
        return r
        
class Solution2:
    def minOperations(self, nums: list[int], x: int, y: int) -> int:
        def predicate(ops: int) -> bool:
            return sum(max(0, math.ceil((num - ops * y) / (x - y)))
                       for num in nums) <= ops

        return bisect.bisect_left(range(max(nums)), True, key=predicate)