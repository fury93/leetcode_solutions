# Approach 1: Min-Heap
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = [] # We'll use heapq to treat this as a min-heap.
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            # If this is actually a "jump down", skip it.
            if climb <= 0:
                continue
            # Otherwise, allocate a ladder for this climb.
            heapq.heappush(ladder_allocations, climb)
            # If we haven't gone over the number of ladders, nothing else to do.
            if len(ladder_allocations) <= ladders:
                continue
            # Otherwise, we will need to take a climb out of ladder_allocations
            bricks -= heapq.heappop(ladder_allocations)
            # If this caused bricks to go negative, we can't get to i + 1
            if bricks < 0:
                return i
        # If we got to here, this means we had enough to cover every climb.
        return len(heights) - 1

# Approach 3: Binary Search for Final Reachable Building
class Solution3:

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        # Helper function to check whether or not the specified building is reachable
        # from the first building with the bricks and ladders we have.
        def is_reachable(building_index):
            # Make a sorted list of all the climbs needed to get to the given building.
            climbs = []
            for h1, h2 in zip(heights[:building_index], heights[1:building_index + 1]):
                if h2 - h1 > 0:
                    climbs.append(h2 - h1)
            climbs.sort()
            # Check whether or not we have enough bricks and ladders to cover all
            # of these climbs. Bricks will be used before ladders.
            bricks_remaining = bricks
            ladders_remaining = ladders
            for climb in climbs:
                # If there are enough bricks left, use those.
                if climb <= bricks_remaining:
                    bricks_remaining -= climb
                # Otherwise, you'll have to use a ladder.
                elif ladders_remaining >= 1:
                    ladders_remaining -= 1
                # And if there are no ladders either, we can't reach buildingIndex.
                else:
                    return False
            return True
         
        # Do the binary search to find the final reachable building.
        lo = 0
        hi = len(heights) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if is_reachable(mid):
                lo = mid
            else:
                hi = mid - 1
        return hi # Note that return lo would be equivalent.       

# Approach 5: Binary Search on Threshold (Advanced)
class Solution5:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        def solveWithGivenThreshold(K):
            
            ladders_remaining = ladders
            bricks_remaining = bricks
            ladders_used_on_threshold = 0
            
            for i in range(len(heights) - 1):
                climb = heights[i + 1] - heights[i]
                if climb <= 0:
                    continue
                    
                # Make resource allocations
                if climb == K:
                    ladders_used_on_threshold += 1
                    ladders_remaining -= 1
                elif climb > K:
                    ladders_remaining -= 1
                else:
                    bricks_remaining -= climb
                    
                # Handle negative resources.
                if ladders_remaining < 0:
                    if ladders_used_on_threshold:
                        ladders_used_on_threshold -= 1
                        ladders_remaining += 1
                        bricks_remaining -= K
                    else:
                        return [i, ladders_remaining, bricks_remaining]
                
                if bricks_remaining < 0:
                    return [i, ladders_remaining, bricks_remaining]
            
            return [len(heights) - 1, ladders_remaining, bricks_remaining]
                
        
        # Find the minimum climb and maximum climbs
        lo = math.inf
        hi = -math.inf
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            lo = min(lo, climb)
            hi = max(hi, climb)
        
        if lo == math.inf: # Was there no climbs?
            return len(heights) - 1
        
        # Carry out the binary search.
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            index_reached, ladders_remaining, bricks_remaining = solveWithGivenThreshold(mid)
            # Did we get all the way?
            if index_reached == len(heights) - 1:
                return len(heights) - 1
            # Otherwise, if we have a ladder remaining, it has to be too high.
            if ladders_remaining > 0:
                hi = mid - 1
                continue
                
            # Otherwise, check for the other optimal conditions.
            next_climb = heights[index_reached + 1] - heights[index_reached]
            if bricks_remaining < next_climb and bricks_remaining < mid:
                return index_reached
            
            # Otherwise, it must have been too low.
            lo = mid + 1
