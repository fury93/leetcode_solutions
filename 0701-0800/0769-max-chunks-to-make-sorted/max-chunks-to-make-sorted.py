class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        chunks = 0
        max_element = 0

        for i in range(n):
            max_element = max(max_element, arr[i])

            if max_element == i:
                chunks += 1

        return chunks