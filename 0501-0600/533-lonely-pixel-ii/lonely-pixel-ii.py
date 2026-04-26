class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        m, n = len(picture), len(picture[0])
        freq = defaultdict(int)
        rows = [0] * m
        cols = [0] * n
        for i in range(m): 
            for j in range(n): 
                if picture[i][j] == "B": 
                    rows[i] += 1
                    cols[j] += 1
            freq["".join(picture[i])] += 1
        
        ans = 0
        for i in range(m):
            key = "".join(picture[i])
            if freq[key] == target: 
                for j in range(n): 
                    if picture[i][j] == "B" and rows[i] == cols[j] == target: ans += 1
        return ans 

# class Solution:
#     def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
#         R, C = len(picture), len(picture[0])
#         blackRows, blackCols = [0] * R, [0] * C
#         for i, j in product(range(R), range(C)):
#             if picture[i][j] == 'B':
#                 blackRows[i] += 1
#                 blackCols[j] += 1
        
#         targetRows = sum(cnt == target for cnt in blackRows)
#         targetCols = sum(cnt == target for cnt in blackCols)

#         return targetRows * targetCols


#         [
#             ["W","B","W","B","B","W"], 3
#             ["W","B","W","B","B","W"], 3
#             ["W","B","W","B","B","W"], 3
#             ["B","W","B","W","W","B"]. 3
#         ].    1.  3.  1.  3.  3.  1