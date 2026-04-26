class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if target == mat:
                return True
            mat = list(map(list, zip(*mat[::-1])))
            #mat = [list(x) for x in zip(*reversed(mat))]
        return False