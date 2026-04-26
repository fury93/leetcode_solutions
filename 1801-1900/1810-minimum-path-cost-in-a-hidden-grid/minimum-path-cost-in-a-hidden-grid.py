# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> int:
#        
#
#    def isTarget(self) -> bool:
#        
#

class Solution:
    DIR = ['U', 'R', 'D', 'L']
    STEPS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self):
        self.map = {}
        self.target = None

    def findShortestPath(self, master):
        # DFS to map out the grid
        self.dfs(master, 0, 0)
        
        if self.target is None:
            return -1

        # Priority Queue for shortest path
        pq = [(0, 0, 0)]  # (cost, x, y)
        while pq:
            cur_cost, x, y = heapq.heappop(pq)
            if (x, y) == self.target:
                return cur_cost
            for step in self.STEPS:
                x1, y1 = x + step[0], y + step[1]
                if (x1, y1) not in self.map:
                    continue
                val = self.map.pop((x1, y1))
                heapq.heappush(pq, (cur_cost + val, x1, y1))

        return -1

    def dfs(self, master, x, y):
        if master.isTarget():
            self.target = (x, y)
        for i in range(4):
            x1, y1 = x + self.STEPS[i][0], y + self.STEPS[i][1]
            if (x1, y1) not in self.map and master.canMove(self.DIR[i]):
                val = master.move(self.DIR[i])
                self.map[(x1, y1)] = val
                self.dfs(master, x1, y1)
                master.move(self.DIR[(i + 2) % 4])

class Solution2:
    def findShortestPath(self, master: 'GridMaster') -> int:
        opposite = {'D': 'U', 'U': 'D', 'L': 'R', 'R': 'L'}       # opposite direction to move back and force
        cost_dict = collections.defaultdict(lambda: sys.maxsize)  # save cost for each location (x, y)
        target = None                                             # this will be `target` index
        
        def dfs(cur, x, y):
            nonlocal target
            if cur.isTarget():                                    # if `target` found, save its index and return True
                target = x, y
                return True
            ans = False
            for di, (i, j) in zip(['D', 'U', 'L', 'R'], [(-1, 0), (1, 0), (0, -1), (0, 1)]): # explore 4 directions
                _x, _y = x+i, y+j
                if (_x, _y) in cost_dict: continue                # check if (_x, _y) is visited
                cost_dict[(_x, _y)] = sys.maxsize                 # mark (_x, _y) as visited
                if cur.canMove(di):
                    cost = cur.move(di)                           # move to direction `di`
                    cost_dict[(_x, _y)] = cost                    # save cost of (_x, _y)
                    ans |= dfs(cur, _x, _y)                       # `dfs`
                    cur.move(opposite[di])                        # move back
            return ans                    
        
        if not dfs(master, 0, 0): return -1                       # if can't reach to `target`, return -1
        
        heap = [(0, 0, 0)]                                        # starts from (0, 0) again. Parameters are (cost, x, y)
        while heap:                                               # Dijkstra starts here
            cost, x, y = heapq.heappop(heap)
            if (x, y) == target: return cost
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _x, _y = x+i, y+j
                if (_x, _y) not in cost_dict: continue            # if location not in `cost_dict`, meaning it's not accessible
                heapq.heappush(heap, (cost+cost_dict[(_x, _y)], _x, _y))
                cost_dict[(_x, _y)] = sys.maxsize                 # mark as visited
        return -1