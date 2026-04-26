class SummaryRanges:

    def __init__(self):
        self.nums = [False] * 100001

    def addNum(self, value: int) -> None:
        self.nums[value] = True

    def getIntervals(self) -> List[List[int]]:
        res = []
        for n, exist in enumerate(self.nums):
            if not exist: continue
            if res and res[-1][1] == n - 1:
                res[-1][1] = n
            else:
                res.append([n, n])
        return res

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()