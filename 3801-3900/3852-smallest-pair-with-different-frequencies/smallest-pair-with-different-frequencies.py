class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        x = min(cnt.keys())
        sortByFreq = sorted(cnt, key = cnt.get)

        for y, freq in sorted(cnt.items(), key=lambda key: (cnt[key], key)):
            if y > x and cnt[x] != cnt[y]:
                return [x, y]

        return [-1, -1]