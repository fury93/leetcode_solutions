class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res, pos = math.inf, dict()

        for i3, n in enumerate(nums):
            if n in pos:
                i1, i2 = pos[n]
                if i1 is not None:
                    res = min(res, (i3 - i1) * 2)
                pos[n] = (i2, i3)
            else:
                pos[n] = (None, i3)

        return -1 if res == math.inf else res

    def minimumDistance2(self, nums: List[int]) -> int:
        res, cnt = math.inf, defaultdict(list)

        for i, n in enumerate(nums):
            if n in cnt and len(cnt[n]) >= 2:
                res = min(res, (i - cnt[n][-2]) * 2)
            cnt[n].append(i)

        return -1 if res == math.inf else res