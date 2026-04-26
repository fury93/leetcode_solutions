class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(k*v for k,v in Counter(s).most_common())