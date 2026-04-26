class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.valToIndexes = defaultdict(list)
        for idx, val in enumerate(arr):
            self.valToIndexes[val].append(idx)

    def query(self, left: int, right: int, value: int) -> int:
        indexes =  self.valToIndexes[value]
        leftIdx = bisect_left(indexes, left)
        rightIdx = bisect_right(indexes, right)
        return rightIdx - leftIdx


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)