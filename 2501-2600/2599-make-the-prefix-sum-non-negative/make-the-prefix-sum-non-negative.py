class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        cur, ans, heap = 0, 0, []
        for num in nums:
            heapq.heappush(heap, num)      # keep tracking minimum
            cur += num                     # prefix sum
            if cur < 0:                    # if prefix sum < 0: 
                ans += 1                   #   increment operation count 
                cur -= heapq.heappop(heap) #   remove the smallest value seen so far
        return ans