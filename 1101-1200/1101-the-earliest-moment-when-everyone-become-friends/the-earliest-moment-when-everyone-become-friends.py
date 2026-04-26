# https://codeforces.com/blog/entry/15296
# https://www.reddit.com/r/leetcode/comments/1gifxtk/google_interview_problem_everyone_is_getting/
# Follow-up:
# Two types of logs
# Add Friend - A and B become friends
# Remove Friend - If A and B are friends, unfriend them
# Two people can be connected and disconnected multiple times.
# Given this, find the earliest timestamp when all of them become friends

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        relationsRemaining = n-1
        if len(logs) < relationsRemaining: return -1
        
        uf = UnionFind(n)
        for time, fr1, fr2 in sorted(logs, key = lambda x: x[0]):
            if not uf.connected(fr1, fr2):
                uf.union(fr1, fr2)
                relationsRemaining -= 1
            if relationsRemaining == 0: return time

        return -1

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