class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d, res = defaultdict(int), -1
        for n in nums:
            if n & 1: continue
            d[n] += 1
            if d[n] > d[res] or (d[n] == d[res] and n < res):
                res = n
        
        return res
