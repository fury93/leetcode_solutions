N = 10**6 + 1
lpf = list(range(N))

for i in range(2, math.isqrt(N)+1, 1):
    if lpf[i] == i:
        for j in range(i*i, N, i):
            if lpf[j] == j:
                lpf[j] = i

class Solution:
    # with precomputation of lpf(least prime factors)
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= nums[i+1]: continue
            nums[i] = lpf[nums[i]]
            if nums[i] > nums[i+1]: return -1
            res += 1
        return res

    def minOperations2(self, nums: List[int]) -> int:
        @cache
        def getLowestFactor(n):
            if n % 2 == 0: return 2

            for d in range(3, math.isqrt(n)+1, 1):
                if n % d == 0:
                     return d
            return n

        res = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                nums[i] = getLowestFactor(nums[i])
                if nums[i] > nums[i+1]:
                    return -1
                res += 1

        return res