class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        ans = prefix = 0
        seen = {0: -1}
        for i in range(len(nums1)): 
            prefix += nums1[i] - nums2[i]
            if prefix in seen: ans = max(ans, i - seen[prefix])
            seen.setdefault(prefix, i)
        return ans 