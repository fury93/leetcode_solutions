class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return (Counter(nums1) & Counter(nums2)).elements()

    def intersect3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res, cnt1, cnt2 = [], Counter(nums1), Counter(nums2)
        for n, k in cnt1.items():
            if n in cnt2:
                res.extend([n]*min(k, cnt2[n]))
        return res
        
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i +=1
            elif nums1[i] > nums2[j]:
                j +=1
            else:
                res.append(nums1[i])
                i +=1
                j +=1

        return res