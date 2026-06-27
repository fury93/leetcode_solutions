class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = cnt[1] - (cnt[1] % 2 ^ 1)
        del cnt[1]
        for x in cnt:
            t = 0
            while cnt[x] > 1:
                x = x * x
                t += 2
            t += 1 if cnt[x] else -1
            ans = max(ans, t)
        return ans

    def maximumLength2(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        one_cnt = cnt.get(1, 0)
        ans = one_cnt if one_cnt % 2 else one_cnt - 1

        cnt.pop(1, None)

        for num in cnt:
            res = 0
            x = num
            while x in cnt and cnt[x] > 1:
                res += 2
                x *= x
            ans = max(ans, res + (1 if x in cnt else -1))

        return ans