class Solution:
    def minSwaps2(self, data: List[int]) -> int:
        ones = sum(data)
        if ones == 0: return 0
        res = zeros = ones - sum(data[:ones])
        for i in range(ones, len(data)):
            zeros += data[i] == 0
            zeros -= data[i-ones] == 0
            res = min(res, zeros)
        return res

    def minSwaps(self, data: List[int]) -> int:
        res, zeros, ones = math.inf, 0, sum(data)
        if ones <= 1: return 0

        # to get rid of r + 1 use start = 1
        for r, n in enumerate(data):
            zeros += n == 0
            if r + 1 < ones: continue
            res = min(res, zeros)
            zeros -= data[r + 1 - ones] == 0
        
        return res