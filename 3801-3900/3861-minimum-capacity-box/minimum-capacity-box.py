class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        res_id = -1
        for i, size in enumerate(capacity):
            if itemSize <= size:
                if res_id == -1 or size < capacity[res_id] :
                    res_id = i

        return res_id