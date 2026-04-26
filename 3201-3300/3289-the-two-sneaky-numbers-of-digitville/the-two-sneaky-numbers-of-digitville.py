class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
            if count[x] == 2:
                res.append(x)
        return res
        
    def getSneakyNumbers2(self, nums: List[int]) -> List[int]:
        uniqNumsCnt = len(nums)-2
        xorNums = reduce(xor, nums)
        xorKeys = reduce(xor, range(uniqNumsCnt))
        xorDuplicates = xorNums ^ xorKeys
        firstDiffBit = xorDuplicates & -xorDuplicates # read more about negative bit representations

        group1Nums = reduce(xor, (n for n in nums if n & firstDiffBit))
        group1Keys = reduce(xor, (i for i in range(uniqNumsCnt) if i & firstDiffBit))

        group2Nums = reduce(xor, (n for n in nums if not n & firstDiffBit))
        group2Keys = reduce(xor, (i for i in range(uniqNumsCnt) if not i & firstDiffBit))

        return [group1Nums ^ group1Keys, group2Nums ^ group2Keys]

        