class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        freq = defaultdict(int)
        acc = defaultdict(int)
        freq[0], acc[0] = 1, 1

        bal = 0
        res = 0

        for num in nums:
            if num == target: bal += 1
            else: bal -= 1
            
            freq[bal] += 1
            acc[bal] = acc[bal - 1] + freq[bal]
            res += acc[bal - 1]

        return res
        
    def countMajoritySubarrays2(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pre = [0] * (n * 2 + 1)
        pre[n] = 1
        cnt = n
        ans = presum = 0
        for i in range(n):
            if nums[i] == target:
                presum += pre[cnt]
                cnt += 1
                pre[cnt] += 1
            else:
                cnt -= 1
                presum -= pre[cnt]
                pre[cnt] += 1
            ans += presum
        return ans