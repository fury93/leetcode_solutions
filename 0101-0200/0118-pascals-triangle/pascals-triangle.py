class Solution:
    def generate2(self, numRows: int) -> List[List[int]]:
        res = [[1]*(i+1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
                
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            prev = res[i-1]
            row = [a+b for a,b in zip(chain([0], prev), chain(prev, [0]))]
            res.append(row) 
            
        return res