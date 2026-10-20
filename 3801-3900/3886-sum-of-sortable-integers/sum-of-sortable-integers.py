def sum_sortable_k(nums):
    n = len(nums)
    descents = [a > b for a, b in pairwise(nums)]

    def is_sortable(k):
        maximum = 0
        for i in range(0, n, k):
            e = i + k - 1
            window_sum = sum(descents[i:e]) + (nums[e] > nums[i])
            if window_sum > 1:
                return False
            local_minimum, local_maximum = min(nums[i:e + 1]), max(nums[i:e + 1])
            if local_minimum < maximum:
                return False
            maximum = max(maximum, local_maximum)
        return True
    return sum(k for k in range(1, n + 1) if n % k == 0 and is_sortable(k))

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        return sum_sortable_k(nums)
            

class Solution2:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        fac = []
        for x in range(1, isqrt(n) + 1):
            if n % x == 0:
                fac.append(x)
                if n // x != x:
                    fac.append(n // x)

        target = sorted(nums)

        def kmp(nums1, nums2):
            n, m = len(nums1), len(nums2)

            pi = [0] * m
            j = 0

            for i in range(1, m):
                while j > 0 and nums2[i] != nums2[j]:
                    j = pi[j - 1]

                if nums2[i] == nums2[j]:
                    j += 1

                pi[i] = j

            j = 0
            for i in range(n):
                while j > 0 and nums1[i] != nums2[j]:
                    j = pi[j - 1]

                if nums1[i] == nums2[j]:
                    j += 1

                if j == m:
                    return True

            return False

        def check(nums1, nums2):
            return kmp(nums1 + nums1, nums2)

        ans = 0

        for d in fac:
            for left in range(0, n, d):
                right = left + d - 1

                if not check(nums[left : right + 1], target[left : right + 1]):
                    break
            else:
                ans += d

        return ans