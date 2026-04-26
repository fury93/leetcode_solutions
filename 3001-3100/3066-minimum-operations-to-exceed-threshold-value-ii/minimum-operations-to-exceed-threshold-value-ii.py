class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = list(filter(lambda n: n < k, nums))
        heapify(nums)

        res = 0
        while len(nums) > 1:
            n1 = heappop(nums)
            n2 = heappop(nums)
            n3 = n1 * 2 + n2
            if n3 < k:
                heappush(nums, n3)
            res += 1

        return res + len(nums)
