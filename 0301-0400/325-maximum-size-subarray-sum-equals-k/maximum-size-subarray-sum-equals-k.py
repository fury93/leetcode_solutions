class Solution:
    #prefixSum[j] - prefixSum[i] = k => prefixSum[j] - k = prefixSum[i]
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        res, pos, sm = 0, {0: -1}, 0
        for i, n in enumerate(nums):
            sm += n
            if sm not in pos:
                pos[sm] = i
            if sm - k in pos:
                res = max(res, i - pos[sm-k])
        return res

class Solution2:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = longest_subarray = 0
        indices = {}
        
        for i, num in enumerate(nums):
            prefix_sum += num
            
            # Check if all of the numbers seen so far sum to k.
            if prefix_sum == k:
                longest_subarray = i + 1
                
            # If any subarray seen so far sums to k, then
            # update the length of the longest_subarray. 
            if prefix_sum - k in indices:
                longest_subarray = max(longest_subarray, i - indices[prefix_sum - k])
                
            # Only add the current prefix_sum index pair to the 
            # map if the prefix_sum is not already in the map.
            if prefix_sum not in indices:
                indices[prefix_sum] = i
        
        return longest_subarray