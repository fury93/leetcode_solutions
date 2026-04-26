class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for val in cnt.values():
            if val > 1:
                res += (val * (val-1)) //2
        return res

    def numIdenticalPairs2(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        ans = 0
        for num in nums:
            ans += counts[num]
            counts[num] += 1
        
        return ans