class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        pos = k
        while volume > 0:
            while pos - 1 >= 0 and heights[pos - 1] <= heights[pos]:
                pos -= 1

            while pos + 1 < len(heights) and heights[pos + 1] <= heights[pos]:
                pos += 1
            
            while pos > k and heights[pos] == heights[pos - 1]:
                pos -= 1

            heights[pos] += 1
            volume -= 1
        
        return heights


class Solution2:
    def pourWater(self, heights, V, K):
        for _ in range(V):
            index = -1
            for i in range(K-1, -1, -1):
                if heights[i] > heights[i+1]:
                    break
                elif heights[i] < heights[i+1]:
                    index = i
            if index != -1:
                heights[index] += 1
                continue

            index = -1
            for i in range(K+1, len(heights)):
                if heights[i] > heights[i-1]:
                    break
                elif heights[i] < heights[i-1]:
                    index = i
            if index != -1:
                heights[index] += 1
            else:
                heights[K] += 1
        return heights