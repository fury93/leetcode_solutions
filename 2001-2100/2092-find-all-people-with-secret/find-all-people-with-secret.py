class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        uf = UnionFind(n)
        uf.union(0, firstPerson)

        meetingGroups = defaultdict(list)
        for x, y, time in meetings:
            meetingGroups[time].append([x, y])

        for t in sorted(meetingGroups.keys()):
            for x, y in meetingGroups[t]:
                uf.union(x, y)
            
            for x, y in meetingGroups[t]:
                if not uf.connected(x, firstPerson):
                    uf.reset(x)
                    uf.reset(y)
        
        return list(filter(lambda x: uf.connected(x, firstPerson), range(n)))

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def reset(self, x: int) -> None:
        self.root[x] = x
        self.rank[x] = 0