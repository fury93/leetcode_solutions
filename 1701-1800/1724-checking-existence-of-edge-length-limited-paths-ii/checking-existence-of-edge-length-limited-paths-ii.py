class PersistentUnionFind:
    def __init__(self, n):
        self.rank = [0] * n
        self.p = list(range(n))
        self.version = [inf] * n

    def find(self, x, t=inf):
        if self.p[x] == x or self.version[x] >= t:
            return x
        return self.find(self.p[x], t)

    def union(self, a, b, t):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] > self.rank[pb]:
            self.version[pb] = t
            self.p[pb] = pa
        else:
            self.version[pa] = t
            self.p[pa] = pb
            if self.rank[pa] == self.rank[pb]:
                self.rank[pb] += 1
        return True


class DistanceLimitedPathsExist:
    def __init__(self, n: int, edgeList: List[List[int]]):
        self.puf = PersistentUnionFind(n)
        edgeList.sort(key=lambda x: x[2])
        for u, v, dis in edgeList:
            self.puf.union(u, v, dis)

    def query(self, p: int, q: int, limit: int) -> bool:
        return self.puf.find(p, limit) == self.puf.find(q, limit)
        
class DistanceLimitedPathsExist2:

    def __init__(self, n, edgeList):
        def find(node):
            if parent[node]!=node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(x,y):
            parent[find(y)] = find(x)
            return
        
        parent = {i:i for i in range(n)}# parent for each node
        edgeList.sort(key = lambda x:x[2])
        self.connections = []
        self.weights = []
        for index,(i,j,weight) in enumerate(edgeList):# for cur weight, connect i,j
            union(i,j)
            if index!=len(edgeList)-1 and weight == edgeList[index+1][2]:
                continue
            self.weights.append(weight) # save the weight keys
            self.connections.append([find(i) for i in parent])# save the connection for cur weight
            

    def query(self, p, q, limit):
        index = bisect.bisect_left(self.weights,limit)
        if index==0:
            return False
        return self.connections[index-1][p] == self.connections[index-1][q]     


# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)