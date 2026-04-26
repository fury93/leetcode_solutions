class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        deq = map(deque, mat)

        for i, row in enumerate(deq):
            
            shifted = row.copy()
            shifted.rotate(k)

            if row != shifted: return False

        return True