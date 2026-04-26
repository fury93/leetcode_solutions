class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        t1, t2 = tree
        s1, s2 = squirrel
        res = 0
        
        def get_dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        min_dist = float('inf')
        for n in nuts:
            dist = get_dist(tree, n)
            min_dist = min(min_dist, get_dist(squirrel, n) - dist)
            res += 2*dist
        res += min_dist
        return res
        
class Solution2:
    def minDistance(self, height, width, tree, squirrel, nuts):
        def taxi(p, q):
            return abs(p[0] - q[0]) + abs(p[1] - q[1])
        
        S = sum(2 * taxi(tree, nut) for nut in nuts)
        return min(S + taxi(squirrel, nut) - taxi(nut, tree) for nut in nuts)