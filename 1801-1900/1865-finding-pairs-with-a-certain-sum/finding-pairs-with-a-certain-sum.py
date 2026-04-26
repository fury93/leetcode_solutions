class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1Cnt = Counter(nums1)
        self.nums2Cnt = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        oldVal = self.nums2[index]
        self.nums2[index] += val
        self.nums2Cnt.update({self.nums2[index]: 1, oldVal: -1})

    def count(self, tot: int) -> int:
        res = 0
        for n1, n1Cnt in self.nums1Cnt.items():
            n2 = tot - n1
            if n2 in self.nums2Cnt:
                res += self.nums2Cnt[n2] * n1Cnt
        return res
        
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)