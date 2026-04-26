# The same (846. Hand of Straights): https://leetcode.com/problems/hand-of-straights/
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        cnt = Counter(nums)

        for val in sorted(cnt):
            if not cnt[val]: continue
            groupCnt = cnt[val]
            for j in range(val, val + k):
                if cnt[j] < groupCnt:
                    return False
                cnt[j] -= groupCnt

        return True