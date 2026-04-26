class Solution:
    def largestCombination(self, candidates):
        freq = [0] * 24 # 2**24 > 10**7 (max possible value)
        for n in candidates:
            for i in range(24):
                if n & (1 << i):
                    freq[i] += 1

        return max(freq)