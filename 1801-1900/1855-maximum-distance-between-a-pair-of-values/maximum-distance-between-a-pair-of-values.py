class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res, nums2 = 0, [-x for x in nums2]

        for i, n in enumerate(nums1):
            j = bisect_right(nums2, -n, i, len(nums2))
            res = max(res, j - i - 1)
        
        return res
