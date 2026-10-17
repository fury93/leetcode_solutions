class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Sorting by (digit sum, value) fixes where each element must end up; a permutation
        # made of c cycles needs len - c swaps.
        n = len(nums)
        order = sorted(range(n), key=lambda i: (sum(map(int, str(nums[i]))), nums[i]))
        seen = [False] * n
        cycles = 0
        for i in range(n):
            if seen[i]:
                continue
            cycles += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = order[j]
        return n - cycles
        
class Solution2:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        digitSum = [0] * n
        for i, v in enumerate(nums):
            s = 0
            while v > 0:
                s += v % 10
                v //= 10
            digitSum[i] = s

        indices = list(range(n))
        indices.sort(key=lambda i: (digitSum[i], nums[i]))

        targetPos = [0] * n
        for pos, idx in enumerate(indices):
            targetPos[idx] = pos

        parent = list(range(n))
        components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(n):
            ri = find(i)
            rj = find(targetPos[i])
            if ri != rj:
                parent[ri] = rj
                components -= 1

        return n - components