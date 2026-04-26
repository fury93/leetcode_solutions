class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        # s = "pfpfgi"
        freq = Counter(s)   # {p: 2, f: 2, g: 1, i: 1}
        freqGroup = Counter(freq.values()) # {2: 2, 1: 2}
        maxFreq = max(freqGroup.keys(), key = lambda g: (freqGroup[g], g)) # max((2,2), (2,1))

        return ''.join(str(ch) for ch in freq if freq[ch] == maxFreq)
