class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt, vowels = Counter(s), "aeiou"
        vow = max((cnt[ch] for ch in cnt if ch in vowels), default=0)
        con = max((cnt[ch] for ch in cnt if ch not in vowels), default=0)
        
        return vow + con