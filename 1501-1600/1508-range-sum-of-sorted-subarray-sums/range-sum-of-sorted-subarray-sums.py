class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        h = [(x, i) for i, x in enumerate(nums)] #min-heap 
        heapify(h)
        
        ans = 0
        for k in range(1, right+1): #1-indexed
            x, i = heappop(h)
            if k >= left: ans += x
            if i+1 < len(nums): 
                heappush(h, (x + nums[i+1], i+1))
                
        return ans % 1_000_000_007