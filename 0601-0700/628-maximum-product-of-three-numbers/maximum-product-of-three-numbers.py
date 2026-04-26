class Solution:
    # First, k items are heapified - that's an O(k*log(k)) operation.
    # Then, n-k items are added into the heap with heapreplace - that's n-k O(log(k)) operations, or O((n-k)log(k)).
    # Add those up, you get O(nlog(k)).
    # In this case k is constant and doesn't scale with n, so this usage is O(n).
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        mx = heapq.nlargest(3, nums)
        mn = heapq.nsmallest(2, nums)

        return max(mx[0] * mx[1] * mx[2], mn[0] * mn[1] * mx[0])

    # N*log(N)
    def maximumProduct2(self, nums: List[int]) -> int:
        def mult(arr):
            return reduce(lambda x, y: x * y, arr)
        
        if len(nums) == 3: return mult(nums)
        nums.sort()

        return max(mult(nums[:2] + [nums[-1]]), mult(nums[-3::]))
