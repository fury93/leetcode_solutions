class Solution:
    def subarraysDivByK2(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        count = [1] + [0] * k
        for a in nums:
            prefix = (prefix + a) % k
            res += count[prefix]
            count[prefix] += 1
        return res

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d, prefix, res = defaultdict(int, {0: 1}), 0, 0
        for n in nums:
            prefix = (prefix + n) % k
            res += d[prefix]
            d[prefix] +=1

        return res