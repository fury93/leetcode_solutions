class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {n: i for i, n in enumerate(nums2)}

        return [d[n] for n in nums1]
        