class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = [0] * 101
        for n in nums:
            freq[n] += 1

        return sum(freq[i] * freq[i-k] for i in range(k, len(freq)))

        

    def countKDifference2(self, nums: List[int], k: int) -> int:
        res, seen = 0, defaultdict(int)
        for n in nums:
            res += seen[n - k] + seen[n + k]
            seen[n] +=1

        return res

    def countKDifference3(self, nums: List[int], k: int) -> int:
        res, L = 0, len(nums)
        for i in range(L):
            for j in range(i, L):
                if abs(nums[i] - nums[j]) == k:
                    res +=1

        return res