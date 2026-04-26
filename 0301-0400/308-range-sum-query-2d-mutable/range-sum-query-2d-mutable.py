class BIT:
    def __init__(self,  nums: List[int]) -> None:
        self.nums = nums
        self.n = len(nums) + 1
        self.tree = [0] + nums
        for i in range(1, self.n):
            p = i + (i & -i)
            if p < self.n:
                self.tree[p] += self.tree[i]
    
    def query(self, i: int) -> int:
        i += 1
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def update(self, i: int, v: int) -> None:
        d = v - self.nums[i]
        self.nums[i] = v
        i += 1
        while i < self.n:
            self.tree[i] += d
            i += i & -i
        
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0])
        self.bits = [BIT(row) for row in matrix]

    def update(self, row: int, col: int, val: int) -> None:
        self.bits[row].update(col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2 + 1):
            total += self.bits[r].query(col2) - self.bits[r].query(col1 - 1)
        return total
        
class NumMatrix3(object):
    def __init__(self, matrix):
        if not matrix:
            return
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix, self.bit = [[0]*(self.n) for _ in range(self.m)], [[0]*(self.n+1) for _ in range(self.m+1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        diff, self.matrix[row][col], i = val-self.matrix[row][col], val, row+1
        while i <= self.m:
            j = col+1
            while j <= self.n:
                self.bit[i][j] += diff
                j += (j & -j)
            i += (i & -i)
        
    def sumRegion(self, row1, col1, row2, col2):
        return self.sumCorner(row2, col2) + self.sumCorner(row1-1, col1-1) - self.sumCorner(row1-1, col2) - self.sumCorner(row2, col1-1)
        
    def sumCorner(self, row, col):
        res, i = 0, row+1
        while i:
            j = col+1
            while j:
                res += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res

class SegmentTreeNode:
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sum = sum

class NumMatrix2:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.m, self.n = len(matrix), len(matrix[0])
        self.root = self.build(matrix, 0, self.m * self.n - 1)
        
    def update(self, row: int, col: int, val: int) -> None:
        index = row * self.n + col
        self.updateTree(self.root, index, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            start = i * self.n + col1
            end = i * self.n + col2
            res += self.queryTree(self.root, start, end)
        return res
        
    def build(self, A, start, end):
        if start > end:
            return None
        
        x, y = divmod(start, self.n)
        root = SegmentTreeNode(start, end, A[x][y])
        if start == end:
            return root
        
        mid = (start + end) // 2
        root.left = self.build(A, start, mid)
        root.right = self.build(A, mid + 1, end)  
        root.sum = root.left.sum + root.right.sum
        return root
    
    def updateTree(self, root, index, val):
        if not root:
            return
        
        if root.start == root.end:
            if root.start == index:
                root.sum = val
            return
        
        mid = (root.start + root.end) // 2
        if index <= mid:
            self.updateTree(root.left, index, val)
        else:
            self.updateTree(root.right, index, val)
        root.sum = root.left.sum + root.right.sum
    
    def queryTree(self, root, start, end):
        if not root:
            return 0
        if start > root.end or end < root.start:
            return 0
        if start <= root.start and end >= root.end:
            return root.sum
        
        mid = (root.start + root.end) // 2
        res = 0
        if start <= mid:
            if end <= mid:
                lSum = self.queryTree(root.left, start, end)
            else:
                lSum = self.queryTree(root.left, start, mid)
            res += lSum
        if end > mid:
            if start > mid:
                rSum = self.queryTree(root.right, start, end)
            else:
                rSum = self.queryTree(root.right, mid + 1, end)
            res += rSum
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)