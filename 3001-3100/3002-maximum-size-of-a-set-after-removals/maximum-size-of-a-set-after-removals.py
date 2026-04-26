class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        set1, set2, maxLen = set(nums1), set(nums2), len(nums1) // 2
        duplicateLen = len(set1 & set2)
        uniqSet1Len = min(maxLen, len(set1) - duplicateLen)
        uniqSet2Len = min(maxLen, len(set2) - duplicateLen)
        
        return min(len(nums1), uniqSet1Len + uniqSet2Len + duplicateLen)
