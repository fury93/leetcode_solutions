class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        ch_map = {chr( i+ ord("a")) : (i+4)//3  for i in range(26)}
        dic = defaultdict(lambda: defaultdict(int))
        for m in range(1,10):
            dic[m][0] = 1
        curr = ans = 0
        for i, ch in enumerate(word, 1):
            curr += ch_map[ch]
            for m in range(1,10):
                ans += dic[m][curr - m*i]
                dic[m][curr - m*i] += 1
        return ans