class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        res = []
        
        for j in range(cols):
            curr_row, curr_col = 0, j
            while curr_row < rows and curr_col < cols:
                index = curr_row * cols + curr_col
                res.append(encodedText[index])
                curr_row += 1
                curr_col += 1
        
        return "".join(res).rstrip()
