class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        for id, n in enumerate(nums):
            if len(minHeap) < k:
                heappush(minHeap, (n, id))
            else:
                heappushpop(minHeap, (n, id))
        
        return [x[0] for x in sorted(minHeap, key=lambda x: x[1])]
