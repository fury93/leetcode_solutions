class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        rows = [[] for _ in range(len(mat))]
        cols = [0] * len(mat[0])
        
        for i in range(len(mat)):
           for j in range(len(mat[0])):
               if mat[i][j]:
                    rows[i].append(j) 
                    cols[j] += 1

        for row in rows:
            if len(row) == 1 and cols[row[0]] == 1:
                res += 1

        return res