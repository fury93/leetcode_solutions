class MRUQueue:

    def __init__(self, n: int):
        self.q = list(range(1, n+1))

    def fetch(self, k: int) -> int:
        self.q.append(self.q.pop(k-1))
        return self.q[-1]
        
class MRUQueue2:

    def __init__(self, n: int):
        self.n = n 
        self.nn = int(sqrt(n))
        self.data = []
        self.index = []
        for i in range(1, n+1):
            ii = (i-1)//self.nn 
            if ii == len(self.data): 
                self.data.append([])
                self.index.append(i)
            self.data[-1].append(i)
            
    def fetch(self, k: int) -> int:
        i = bisect_right(self.index, k)-1
        
        x = self.data[i].pop(k - self.index[i])
        for ii in range(i+1, len(self.index)): # shift index
            self.index[ii] -= 1
        if len(self.data[-1]) >= self.nn: # add new bucket 
            self.data.append([])
            self.index.append(self.n)
        self.data[-1].append(x) # append to bucket at end
        if not self.data[i]: # remove empty bucket 
            self.data.pop(i)
            self.index.pop(i)
        return x


class Fenwick: 
    def __init__(self, n: int): 
        self.nums = [0]*(n+1)
        
    def sum(self, k: int) -> int: 
        ans = 0
        while k: 
            ans += self.nums[k]
            k &= k-1
        return ans 
    
    def add(self, k: int, x: int) -> int: 
        k += 1
        while k < len(self.nums): 
            self.nums[k] += x
            k += k & -k 


class MRUQueue3:

    def __init__(self, n: int):
        self.size = n 
        self.tree = Fenwick(n+2000) # buffer for 2000 calls
        self.vals = [0]*(n+2000)
        for i in range(n):
            self.tree.add(i, 1)
            self.vals[i] = i+1

    def fetch(self, k: int) -> int:
        lo, hi = 0, self.size
        while lo < hi: 
            mid = lo + hi >> 1 
            if self.tree.sum(mid) < k: lo = mid + 1
            else: hi = mid 
        self.tree.add(lo-1, -1)
        self.tree.add(self.size, 1)
        self.vals[self.size] = self.vals[lo-1]
        self.size += 1
        return self.vals[lo-1]

from sortedcontainers import SortedList

class MRUQueue4:

    def __init__(self, n: int):
        self.data = SortedList((i, i) for i in range(1, n+1))

    def fetch(self, k: int) -> int:
        _, x = self.data.pop(k-1)
        i = self.data[-1][0] + 1 if self.data else 0
        self.data.add((i, x))
        return x

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)