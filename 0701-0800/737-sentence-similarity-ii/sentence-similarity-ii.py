class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        uf = UnionFind()
        for w1, w2 in similarPairs:
            uf.union(w1, w2)
        
        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and not uf.connected(w1, w2):
                return False

        return True

class UnionFind:
    def __init__(self):
        self.root = defaultdict(str)
        self.rank = defaultdict(int)

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        self.addIfNotExists(x)
        self.addIfNotExists(y)

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

    def addIfNotExists(self, word):
        if word not in self.root:
            self.root[word] = word
            self.rank[word] = 1

    def connected(self, x, y):
        return x in self.root and y in self.root and self.find(x) == self.find(y)