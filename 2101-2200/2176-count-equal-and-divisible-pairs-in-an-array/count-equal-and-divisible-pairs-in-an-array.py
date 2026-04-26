class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        positions, res = [[] for _ in range(101)], 0
        for i, n in enumerate(nums):
            for j in positions[n]:
                if (i * j) % k == 0:
                    res += 1
            positions[n].append(i)
        return res


