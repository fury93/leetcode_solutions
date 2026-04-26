class Solution:
    def minBuildTime(self, blocks, split):
        n = len(blocks)

        # Sort the blocks in descending order
        blocks.sort(reverse=True)   

        # dp[i][j] represents the minimum time taken to 
        # build blocks[i~n-1] block using j workers
        dp = [[-1] * (n + 1) for _ in range(n)]

        def solve(b, w):
            # Base cases
            if b == n:
                return 0
            if w == 0:
                return float('inf')
            if w >= n - b:
                return blocks[b]

            # If the sub-problem is already solved, return the result
            if dp[b][w] != -1:
                return dp[b][w]

            # Two Choices
            work_here = max(blocks[b], solve(b + 1, w - 1))
            split_here = split + solve(b, min(2 * w, n - b))

            # Store the result in the dp array
            dp[b][w] = min(work_here, split_here)
            return dp[b][w]

        # For block from index 0, with 1 worker
        return solve(0, 1)

class Solution2:
    def minBuildTime(self, blocks: List[int], split: int) -> int:        
        # Sort the blocks in descending order.
        N = len(blocks)
        blocks.sort(reverse=True)
        
        # Initialize the dp array.
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        
        # Base case 1: If there are no workers, then we can't build any block.
        for b in range(N):
            dp[b][0] = float('inf')
        
        # Base case 2: If there are no blocks, then we don't need any time.
        for w in range(N + 1):
            dp[N][w] = 0
        
        # Fill the dp array in a bottom-up fashion.
        for b in range(N - 1, -1, -1):
            for w in range(N, 0, -1):                
                # Base case 3: If we have more workers than blocks, 
                # Then we can build all the blocks.
                if w >= N - b:
                    dp[b][w] = blocks[b]
                    continue

                # Recurrence relation.
                workHere = max(blocks[b], dp[b + 1][w - 1])
                split_here = split + dp[b][min(2 * w, N - b)]
                
                # Store the result in the dp array
                dp[b][w] = min(workHere, split_here)
        
        # For building all the blocks, with 
        # initially 1 worker.
        return dp[0][1]

# Approach 3: Space-Optimized Bottom-up Dynamic Programming
class Solution3:
    def minBuildTime(self, blocks: List[int], split: int) -> int:        
        # Sort the blocks in descending order.
        N = len(blocks)
        blocks.sort(reverse=True)
        
        # Initialize the dp array. When all N blocks
        # done, we need 0 time.
        dp = [0] * (N + 1)

        # The case when we have no workers.
        dp[0] = float('inf')
        
        # Fill the dp array in a bottom-up fashion.
        for b in range(N - 1, -1, -1):
            for w in range(N, 0, -1):                
                # If we have more workers than blocks, 
                # Then we can build all the blocks.
                if w >= N - b:
                    dp[w] = blocks[b]
                    continue

                # Recurrence relation.
                work_here = max(blocks[b], dp[w - 1])
                split_here = split + dp[min(2 * w, N - b)]
                
                # Store the result in the dp array
                dp[w] = min(work_here, split_here)
        
        # For building all the blocks, with 
        # initially 1 worker.
        return dp[1]

# Approach 4: Optimal Merge Pattern
class Solution4:
    def minBuildTime(self, blocks: List[int], split: int) -> int:        
        # Prepare Heap of Building Time
        heapq.heapify(blocks)
        
        # Make sibling blocks until we are left with only one root node
        while len(blocks) > 1:            
            # Pop two minimum. The time of the abstracted sub-root will be 
            # split + max(x, y) which is split + y
            x = heapq.heappop(blocks)
            y = heapq.heappop(blocks)
            heapq.heappush(blocks, split + y)
        
        # Time of final root node
        return heapq.heappop(blocks)

# Approach 5: Binary Search
class Solution5:
    def minBuildTime(self, blocks: List[int], split: int) -> int:        
        # Sort Array in Descending Order of the required time
        blocks.sort(reverse = True)

        # If can be built in "limit"
        def possible(limit):           
            # Build all blocks starting with one worker
            worker = 1

            for index, time in enumerate(blocks):
                # If no worker or no sufficient time
                if worker <= 0 or time > limit:
                    return False
                
                # Keep splitting and producing workers as long as 
                # we are within the limit for this block
                while time + split <= limit:
                    limit -= split
                    worker *= 2

                    # Sufficient workers for the remaining block
                    if worker >= len(blocks) - index:
                        return True
                
                # Build Block
                worker -= 1

            # All blocks build
            return True

        # Binary Search Algorithm
        left = blocks[0]
        right = math.ceil(log2(len(blocks))) * split  + blocks[0]
        while left < right:
            mid = (left + right) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        
        # Right is the minimum time when the task is possible
        return int(right)
