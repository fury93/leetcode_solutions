class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        # create a list of buildings and a set of empty lands for easy search later
        build, land = [], set()
        for x,y in itertools.product(range(len(grid)), range(len(grid[0]))):
            if grid[x][y] == 0:
                land.add((x,y))
            elif grid[x][y] == 1:
                build.append((x,y))
        # if there is no empty land available, we can't proceed further
        if not land:
            return -1
        
        # create a dictionary where each land's position tuple is a key and its value
        # is a list of length equal to the number of buildings we found above. 
        # This list is populated with Inf, to start with, that will be updated by the
        # shortest distance between the land and building pair, found by BFS routine below.
        d = {x: [float('inf')]*len(build) for x in land}
        
        # BFS for a given building's location
        def BFS(loc):
            x, y = build[loc]
            # (x,y) is building's location on the grid and 0 is the starting distance
            q = collections.deque([(x,y,0)]) 
            while q:
                x, y, dist = q.popleft()
                for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    # we are interested in only traversing lands whose recorded distance from
                    # current building is more than dist+1. We update their distance and include
                    # these lands in our queue for the next layer, if that's the case
                    if (i,j) in land and d[(i,j)][loc] > dist + 1:
                        d[(i,j)][loc] = dist + 1
                        q.append((i,j,dist+1))
        
        # run BFS routine for all buildings
        for loc in range(len(build)):
            BFS(loc)
            
        # compute the shortest distance to all buildings for each empty land
        min_dist = min(sum(d[x]) for x in land)
        return -1 if min_dist == float('inf') else min_dist