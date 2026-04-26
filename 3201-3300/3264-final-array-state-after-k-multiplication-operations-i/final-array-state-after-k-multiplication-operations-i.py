class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(n, i) for i, n in enumerate(nums)]
        heapify(heap)

        for _ in range(k):
            val, pos = heappop(heap)
            val *= multiplier
            nums[pos] = val
            heappush(heap, (val, pos))
        
        return nums
