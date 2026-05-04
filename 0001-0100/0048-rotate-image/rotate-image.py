class Solution:
    #1 approach
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = zip(*matrix[::-1])

    # 2 approach
    def rotate2(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        self.transpose(matrix)
        print(matrix)
        #self.reflect(matrix)

    def transpose(self, matrix):
        l = len(matrix[0])
        for i in range(0, l):
            for j in range(i+1, l):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    
    def reflect(self, matrix):
        l = len(matrix[0])
        for i in range (0, l):
            for j in range(0, l//2):
                matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]
            

