class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        
        n = len(s)
        windows = 0

        for unique in range(1, len(set(s)) + 1):
            
            windowSize = unique * count
            if windowSize > n:
                break

            counts = Counter(s[ : windowSize])
            atMostCount = sum([val >= count for val in counts.values()])
            windows += (atMostCount == unique)

            for i in range(windowSize, n):
                counts[s[i - windowSize]] -= 1
                if counts[s[i - windowSize]] == count - 1:
                    atMostCount -= 1
                counts[s[i]] += 1
                if counts[s[i]] == count:
                    atMostCount += 1
                windows += (atMostCount == unique)

        return windows
        
class Solution2:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        ans = 0 
        for k in range(1, 27): 
            freq = Counter()
            uniq = 0 
            for i, ch in enumerate(s): 
                freq[ch] += 1
                if freq[ch] == count: uniq += 1
                if i >= k*count: 
                    if freq[s[i-k*count]] == count: uniq -= 1
                    freq[s[i-k*count]] -= 1
                if uniq == k: ans += 1
        return ans 