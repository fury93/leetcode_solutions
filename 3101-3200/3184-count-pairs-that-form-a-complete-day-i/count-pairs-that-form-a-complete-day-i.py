class Solution:
    # complementary pairs p1 and p2 where p1 + p2 = 24 and p1 != p2 => p1 * p2
    # self-complementary pairs it's 0h and 12h => use formula of combinations without repetition
    # Combinations without repetition: n!/(k!(n-k)! for 2 elements k = 2 equal to sums of pairs: n*(n-1)/2
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        freq = [0] * 24
        for h in hours:
            freq[h%24] += 1

        res = (freq[0] * (freq[0] - 1) + freq[12] * (freq[12] - 1)) // 2
        for h in range(1, 12):
            res += freq[h] * freq[24-h]

        return res

    def countCompleteDayPairs2(self, hours: List[int]) -> int:
        freq = Counter(h % 24 for h in hours)
        
        res = 0
        for h1 in freq:
            h2 = (24 - h1) % 24 # used for 0h
            if h2 not in freq or h1 < h2: continue
            if h1 != h2:
                res += freq[h1] * freq[h2]
            else: 
                res += freq[h1] * (freq[h1] - 1) // 2

        return res
        