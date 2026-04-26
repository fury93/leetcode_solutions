class Solution:
    def maximumLengthSubstring(self, s: str, k = 2) -> int:
        freq, l, moreThanK = defaultdict(int), 0, 0
        
        for ch in s:
            freq[ch] += 1
            moreThanK += freq[ch] == k + 1

            if moreThanK > 0:
                freq[s[l]] -= 1
                moreThanK -= freq[s[l]] == k
                l += 1

        return len(s) - l