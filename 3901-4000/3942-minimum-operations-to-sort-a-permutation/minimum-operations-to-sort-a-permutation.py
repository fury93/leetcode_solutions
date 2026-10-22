class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        best = -1
        s = nums[0]
        if all(nums[i] == (i + s) % n for i in range(n)):
            best = min((n - s) % n, s + 2)
        if all(nums[i] == (s - i) % n for i in range(n)):
            v = 1 + min((s + 1) % n, (n - s - 1) % n)
            if best < 0 or v < best:
                best = v
        return best
        
    def minOperations2(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        start = nums.index(0)

        asc = True
        desc = True

        for i in range(1, n):
            value = nums[(start + i) % n]

            if value != i:
                asc = False
            if value != n - i:
                desc = False

            if not asc and not desc:
                return -1

        if asc:
            return min(start, n - start + 2)

        return min(n - start, start + 2)