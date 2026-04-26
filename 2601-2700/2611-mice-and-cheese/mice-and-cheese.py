class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        points = sum(reward2)
        heap = [] #minHeap, top k cheeses with best profit when replace reward2 with reward1

        for r1, r2 in zip(reward1, reward2):
            profit = r1 - r2
            if len(heap) < k:
                heappush(heap, profit)
            elif heap and heap[0] < profit:
                heapreplace(heap, profit)

        return points + sum(heap)