class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[0, 0]] for _ in range(length)]
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.snapId:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.snapId, val])
        
    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        if self.arr[index][-1][0] == snap_id:
            return  self.arr[index][-1][1]

        idx = bisect.bisect_right(self.arr[index], snap_id, key = lambda x: x[0])
        return self.arr[index][idx-1][1]

        
        return 0 if snap_id < 0 else self.arr[index][snap_id]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)