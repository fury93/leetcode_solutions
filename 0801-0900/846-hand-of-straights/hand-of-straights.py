class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)

        for val in sorted(cnt):
            if not cnt[val]: continue
            groupCnt = cnt[val]
            for j in range(val, val + groupSize):
                if cnt[j] < groupCnt:
                    return False
                cnt[j] -= groupCnt

        return True