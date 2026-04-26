class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapify(heap)

        highVal = max(heap, key = lambda x: x[0])[0]
        res = math.inf, None, None
        while heap:
            lowVal, i, j = heappop(heap)
            curRange = highVal - lowVal
            if curRange < res[0]:
                res = curRange, lowVal, highVal
            if len(nums[i]) == j + 1: break
            newVal = nums[i][j+1]
            highVal = max(highVal, newVal)
            heappush(heap, (newVal, i, j+1))

        return [res[1], res[2]]